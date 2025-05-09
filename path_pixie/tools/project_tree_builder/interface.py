import abc
from typing import Any, Literal


class ITreeBuilder(abc.ABC):
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
        **kwargs: Any,
    ) -> None: ...
