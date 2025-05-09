import abc
from abc import abstractmethod
from dataclasses import dataclass, field


@dataclass
class NodeInfo:
    name: str
    dir_path: str
    full_path: str
    depth: int
    is_dir: bool
    ext: str = ""
    children: list["NodeInfo"] = field(default_factory=list)


class Node(abc.ABC):
    @abstractmethod
    def get_content(self) -> NodeInfo: ...
