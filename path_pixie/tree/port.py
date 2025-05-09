from abc import abstractmethod
from dataclasses import dataclass, field
from typing import Protocol


@dataclass
class LeafContent:
    name: str
    dir_path: str
    full_path: str
    depth: int
    children: list["LeafContent"] = field(default_factory=list)


class Leaf(Protocol):
    @abstractmethod
    def get_content(self) -> LeafContent: ...
