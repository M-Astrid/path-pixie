from abc import abstractmethod
from typing import Any, Protocol

from path_pixie.common.const import DEFAULT_DEPTH
from path_pixie.tree.port import LeafContent


class Renderer(Protocol):
    @abstractmethod
    def __call__(self, content: LeafContent, depth: int = DEFAULT_DEPTH, **kwargs: Any) -> str: ...
