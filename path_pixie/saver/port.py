from abc import abstractmethod
from typing import Protocol


class OutputSaver(Protocol):
    @abstractmethod
    def __call__(self, output: str) -> None: ...
