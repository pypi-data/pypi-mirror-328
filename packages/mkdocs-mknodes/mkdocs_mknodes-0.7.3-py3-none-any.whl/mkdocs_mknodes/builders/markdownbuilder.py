from __future__ import annotations

import os
import pathlib
import tempfile
from typing import TYPE_CHECKING, Any, Literal
from urllib import parse

import logfire
from mkdocs import exceptions
from mkdocs.structure.files import Files
from mkdocs.structure.nav import Navigation, get_navigation
from mkdocs.structure.pages import Page
import mknodes as mk
from mknodes.info import contexts, folderinfo, linkprovider, reporegistry
from mknodes.utils import linkreplacer, pathhelpers

from mkdocs_mknodes import buildcollector, telemetry
from mkdocs_mknodes.backends import markdownbackend, mkdocsbackend
from mkdocs_mknodes.builders import configbuilder
from mkdocs_mknodes.commands import utils
from mkdocs_mknodes.plugin.mknodesconfig import MkNodesConfig


if TYPE_CHECKING:
    pass


logger = telemetry.get_plugin_logger(__name__)
CommandStr = Literal["build", "serve", "gh-deploy"]

DRAFT_CONTENT = (
    '<div class="mkdocs-draft-marker" title="This page wont be included into the site.">'
    "DRAFT"
    "</div>"
)


class MarkdownBuilder:
    """Handles the initial phase of building Websites."""

    def __init__(self, config: MkNodesConfig | None = None):
        """Initialize the markdown builder."""
        self.config = config or MkNodesConfig()
        # Plugin-specific initialization
        self.link_replacer = linkreplacer.LinkReplacer()
        self.build_folder = None
        self._dir = None
        self.linkprovider = None
        self.theme = None
        self.folderinfo = None
        self.context = None
        self.root = None
        self.build_info = None

    def _setup_build_environment(self):
        """Setup build environment from plugin initialization."""
        if self.config.build_folder:
            self.build_folder = pathlib.Path(self.config.build_folder)
        else:
            self._dir = tempfile.TemporaryDirectory(
                prefix="mknodes_",
                ignore_cleanup_errors=True,
            )
            self.build_folder = pathlib.Path(self._dir.name)
            logger.debug("Creating temporary dir %s", self._dir.name)

        if not self.config.build_fn:
            return

        self.linkprovider = linkprovider.LinkProvider(
            base_url=self.config.site_url or "",
            use_directory_urls=self.config.use_directory_urls,
            include_stdlib=True,
        )
        self.theme = mk.Theme.get_theme(
            theme_name=self.config.theme.name or "material",
            data=dict(self.config.theme),
        )
        git_repo = reporegistry.get_repo(
            str(self.config.repo_path or "."),
            clone_depth=self.config.clone_depth,
        )
        self.folderinfo = folderinfo.FolderInfo(git_repo.working_dir)
        self.context = contexts.ProjectContext(
            metadata=self.folderinfo.context,
            git=self.folderinfo.git.context,
            theme=self.theme.context,
            links=self.linkprovider,
            env_config=self.config.get_jinja_config(),
        )

    def build_from_config(
        self,
        config_path: str | os.PathLike[str],
        *,
        site_dir: str | None = None,
        **kwargs: Any,
    ) -> tuple[Navigation, Files]:
        """Build markdown content from config file."""
        cfg_builder = configbuilder.ConfigBuilder()
        cfg_builder.add_config_file(config_path)
        self.config = cfg_builder.build_mkdocs_config(site_dir=site_dir, **kwargs)

        with logfire.span("plugins callback: on_startup", config=self.config):
            self.config.plugins.on_startup(command="build", dirty=False)

        nav, files = self.process_markdown()
        return nav, files

    @utils.handle_exceptions
    @utils.count_warnings
    def process_markdown(self, dirty: bool = False) -> tuple[Navigation, Files]:
        """Process markdown files and build navigation structure."""
        if self.config is None:
            msg = "Configuration must be set before processing markdown"
            raise ValueError(msg)

        with logfire.span("plugins callback: on_config", config=self.config):
            self.config = self.config.plugins.on_config(self.config)
            self._setup_build_environment()

        with logfire.span("plugins callback: on_pre_build", config=self.config):
            self.config.plugins.on_pre_build(config=self.config)

        if not dirty:
            logger.info("Cleaning site directory")
            pathhelpers.clean_directory(self.config.site_dir)

        files = utils.get_files(self.config)
        env = self.config.theme.get_env()
        files.add_files_from_theme(env, self.config)

        # Generate pages if build_fn is specified
        if self.config.build_fn:
            logger.info("Generating pages...")
            build_fn = self.config.get_builder()
            self.root = mk.MkNav(context=self.context)
            build_fn(theme=self.theme, root=self.root)

            mkdocs_backend = mkdocsbackend.MkDocsBackend(
                files=files,
                config=self.config,
                directory=self.build_folder,
            )
            markdown_backend = markdownbackend.MarkdownBackend(
                directory=pathlib.Path(self.config.site_dir) / "src",
                extension=".original",
            )
            collector = buildcollector.BuildCollector(
                backends=[mkdocs_backend, markdown_backend],
                show_page_info=self.config.show_page_info,
                global_resources=self.config.global_resources,
                render_by_default=self.config.render_by_default,
            )
            self.build_info = collector.collect(self.root, self.theme)

        with logfire.span("plugins callback: on_files", files=files, config=self.config):
            files = self.config.plugins.on_files(files, config=self.config)

        utils.set_exclusions(files._files, self.config)
        nav = get_navigation(files, self.config)

        if self.root and (nav_dict := self.root.nav.to_nav_dict()):
            self._update_navigation(nav_dict)

        with logfire.span("plugins callback: on_nav", config=self.config, nav=nav):
            nav = self.config.plugins.on_nav(nav, config=self.config, files=files)
            # Update link replacer mapping
            for file_ in files:
                assert file_.abs_src_path
                filename = pathlib.Path(file_.abs_src_path).name
                url = parse.unquote(file_.src_uri)
                self.link_replacer.mapping[filename].append(url)

        self._process_pages(files)
        return nav, files

    def _update_navigation(self, nav_dict: dict):
        """Update navigation with generated pages."""
        match self.config.nav:
            case list():
                for k, v in nav_dict.items():
                    self.config.nav.append({k: v})
            case dict():
                self.config.nav |= nav_dict
            case None:
                self.config.nav = nav_dict

    def _process_pages(self, files: Files) -> None:
        """Process all pages, reading their content and applying plugins."""
        with logfire.span("populate pages"):
            for file in files.documentation_pages():
                with logfire.span(f"populate page for {file.src_uri}", file=file):
                    logger.debug("Reading: %s", file.src_uri)
                    if file.page is None and file.inclusion.is_not_in_nav():
                        Page(None, file, self.config)
                    assert file.page is not None
                    self._populate_page(file.page, files)

    def _populate_page(self, page: Page, files: Files) -> None:
        """Read page content from docs_dir and render Markdown."""
        try:
            with logfire.span(
                "plugins callback: on_pre_page", page=page, config=self.config
            ):
                page = self.config.plugins.on_pre_page(
                    page, config=self.config, files=files
                )
                # Set edit path from build info if available
                if self.build_info:
                    node = self.build_info.page_mapping.get(page.file.src_uri)
                    edit_path = node._edit_path if isinstance(node, mk.MkPage) else None
                    if path := self.config.get_edit_url(edit_path):
                        page.edit_url = path

            with logfire.span("read_source", page=page):
                page.read_source(self.config)
            assert page.markdown is not None

            with logfire.span(
                "plugins callback: on_page_markdown", page=page, config=self.config
            ):
                page.markdown = self.config.plugins.on_page_markdown(
                    page.markdown, page=page, config=self.config, files=files
                )
                # Apply link replacement
                page.markdown = self.link_replacer.replace(
                    page.markdown, page.file.src_uri
                )

            with logfire.span("render", page=page, config=self.config):
                page.render(self.config, files)
            assert page.content is not None

            with logfire.span(
                "plugins callback: on_page_content", page=page, config=self.config
            ):
                page.content = self.config.plugins.on_page_content(
                    page.content, page=page, config=self.config, files=files
                )
        except Exception as e:
            message = f"Error reading page '{page.file.src_uri}':"
            if not isinstance(e, exceptions.BuildError):
                message += f" {e}"
            logger.exception(message)
            raise
