from typing import Any

from path_pixie.common.const import DEFAULT_DEPTH
from path_pixie.renderer.port import Renderer
from path_pixie.tree.port import NodeInfo


class HTMLRenderer(Renderer):
    def __call__(self, content: NodeInfo, depth: int = DEFAULT_DEPTH, **kwargs: Any) -> str:
        raise NotImplementedError
