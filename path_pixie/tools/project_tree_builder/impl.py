import sys
from typing import Any, Literal

from path_pixie.renderer.adapter.mdlist.enums import Prefix
from path_pixie.renderer.adapter.mdlist.renderer import MDListRenderer
from path_pixie.saver.adapter.file import FileOutputSaver
from path_pixie.tools.project_tree_builder.interface import ITreeBuilder
from path_pixie.tree.adapter.composite import Project


class TreeBuilder(ITreeBuilder):
    def __call__(
        self,
        dir_path: str,
        depth: int = 2,
        *,
        output: str | None = None,
        dir_links: bool = False,
        file_links: bool = True,
        prefix: Literal["emoji", "bullet", "number"] = "bullet",
        start_tag: str = "<!-- path-pixie contents start -->",
        end_tag: str = "<!-- path-pixie contents end -->",
        # exts: list[str] | None = None,  # todo: implement
        # exclude_exts: list[str] | None = None,
        # only_dirs: bool = False,
        # hide_ext: bool = True,
        # name: str | None = None,
        # skip_first: bool = False,
        **kwargs: Any,
    ) -> None:
        project = Project(dir_path)
        tree = project.get_content(
            max_depth=depth,
            # exts: list[str] | None = None,  # todo: implement
            # exclude_exts: list[str] | None = None,
            # only_dirs: bool = False,
            # hide_ext: bool = True,
        )

        render = MDListRenderer(prefix_type=Prefix(prefix))
        formatted = render(
            tree, is_links=True, depth=depth, signoff="Conjured by [path-pixie](https://github.com/path-pixie)"
        )

        if output:
            FileOutputSaver(output, start_tag=start_tag, end_tag=end_tag)(formatted)
        else:
            sys.stdout.write(formatted)
