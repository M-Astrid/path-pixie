import os

from path_pixie.tree.port import Leaf, LeafContent


class FileLeaf(Leaf):
    def __init__(self, name: str, dir_path: str, parent_depth: int = -1, max_depth: int = 0) -> None:
        self.name = name
        self.dir_path = dir_path
        self.depth = parent_depth + 1
        self.max_depth = max_depth

    @property
    def full_path(self) -> str:
        return f"{self.dir_path}/{self.name}"

    def get_content(self) -> LeafContent:
        return LeafContent(
            name=self.name,
            dir_path=self.dir_path,
            full_path=self.full_path,
            depth=self.depth,
        )


class DirectoryLeaf(Leaf):
    def __init__(self, file_name: str, dir_path: str, max_depth: int, parent_depth: int = -1, name: str = None) -> None:
        self.name = name or file_name
        self.file_name = file_name
        self.dir_path = dir_path
        self.depth = parent_depth + 1
        self.max_depth = max_depth

    @property
    def full_path(self) -> str:
        return f"{self.dir_path}/{self.file_name}"

    @property
    def files(self) -> list[str]:
        return os.listdir(self.full_path)

    def get_content(self) -> LeafContent:
        content = LeafContent(
            name=self.file_name,
            dir_path=self.dir_path,
            full_path=self.full_path,
            depth=self.depth,
        )
        if self.depth == self.max_depth:
            return content

        for file in self.files:
            if os.path.isdir(f"{self.full_path}/{file}"):
                leaf_content = DirectoryLeaf(
                    file, self.full_path, max_depth=self.max_depth, parent_depth=self.depth
                ).get_content()
            else:
                leaf_content = FileLeaf(
                    file, self.full_path, max_depth=self.max_depth, parent_depth=self.depth
                ).get_content()
            content.children.append(leaf_content)
        return content


class Project:
    def __init__(self, dir_path: str, name: str = None, skip_first: bool = False):
        self.name = name or dir_path
        self.dir_path = dir_path
        self.skip_first = skip_first

    def get_content(
        self,
        # exts: list[str] | None = None,  # todo: implement
        # exclude_exts: list[str] | None = None,
        # only_dirs: bool = False,
        # hide_ext: bool = True,
        max_depth: int,
    ) -> LeafContent:
        project = DirectoryLeaf(self.dir_path, ".", max_depth=self.max_depth)
        return project.get_content()
