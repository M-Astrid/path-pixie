import abc
from abc import abstractmethod


class OutputSaver(abc.ABC):
    @abstractmethod
    def __call__(self, output: str) -> None: ...
