import abc
from abc import abstractmethod
from typing import Any

from path_pixie.common.const import DEFAULT_DEPTH
from path_pixie.tree.port import NodeInfo


class Renderer(abc.ABC):
    @abstractmethod
    def __call__(self, content: NodeInfo, depth: int = DEFAULT_DEPTH, **kwargs: Any) -> str: ...
