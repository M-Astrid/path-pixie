import sys
from typing import Any, Literal

from path_pixie.renderer.adapter.renderer import MDListRenderer
from path_pixie.saver.adapter.file import FileOutputSaver
from path_pixie.tools.project_tree_generator.port import ITreeGenerator
from path_pixie.tree.adapter.composite import Project


class TreeGenerator(ITreeGenerator):
    async def __call__(
        self,
        dir_path: str,
        max_depth: int = 2,
        *,
        name: str | None = None,
        skip_first: bool = False,
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
        **kwargs: Any,
    ) -> None:
        project = Project("knowledge_base")
        tree = project.get_content(
            max_depth=max_depth,
            # exts: list[str] | None = None,  # todo: implement
            # exclude_exts: list[str] | None = None,
            # only_dirs: bool = False,
            # hide_ext: bool = True,
        )

        render = MDListRenderer()
        formatted = render(tree, is_links=True, depth=max_depth)

        if output:
            FileOutputSaver(output, start_tag=start_tag, end_tag=end_tag)(formatted)
        else:
            sys.stdout.write(formatted)
