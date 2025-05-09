from typing import Any

from path_pixie.common.const import DEFAULT_DEPTH
from path_pixie.renderer.port import Renderer
from path_pixie.tree.port import NodeInfo


class TextRenderer(Renderer):
    prefix_template: str = "{'  '*depth}{char} "
    ident_char: str = "  "
    end_char = "  \n"

    def __call__(self, content: NodeInfo, depth: int = DEFAULT_DEPTH, is_links: bool = False, **kwargs: Any) -> str:
        # content = leaf.get_content()
        # output = self.prefix_template.format(char="└─" if content.depth == 0
        # else "├─", ident=content.depth*self.ident_char)
        raise NotImplementedError
