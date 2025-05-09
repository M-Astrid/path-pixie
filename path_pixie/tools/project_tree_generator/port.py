from typing import Any, Literal, Protocol


class ITreeGenerator(Protocol):
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
        exts: list[str] | None = None,
        exclude_exts: list[str] | None = None,
        only_dirs: bool = False,
        hide_ext: bool = True,
        **kwargs: Any,
    ) -> None: ...
