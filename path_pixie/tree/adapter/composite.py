import os

from path_pixie.tree.port import Node, NodeInfo


class FileNode(Node):
    def __init__(self, name: str, dir_path: str, parent_depth: int = -1, max_depth: int = 0) -> None:
        self.name = name
        self.dir_path = dir_path
        self.depth = parent_depth + 1
        self.max_depth = max_depth

    @property
    def full_path(self) -> str:
        return f"{self.dir_path}/{self.name}"

    @property
    def ext(self) -> str:
        return os.path.splitext(self.name)[1]

    @property
    def raw_name(self) -> str:
        return os.path.splitext(self.name)[0]

    def get_content(self) -> NodeInfo:
        return NodeInfo(
            name=self.raw_name,
            dir_path=self.dir_path,
            full_path=self.full_path,
            depth=self.depth,
            is_dir=False,
            ext=self.ext,
        )


class DirectoryNode(Node):
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

    def get_content(self) -> NodeInfo:
        content = NodeInfo(
            name=self.file_name,
            dir_path=self.dir_path,
            full_path=self.full_path,
            depth=self.depth,
            is_dir=True,
        )
        if self.depth == self.max_depth:
            return content

        for file in self.files:
            if os.path.isdir(f"{self.full_path}/{file}"):
                leaf_content = DirectoryNode(
                    file, self.full_path, max_depth=self.max_depth, parent_depth=self.depth
                ).get_content()
            else:
                leaf_content = FileNode(
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
    ) -> NodeInfo:
        project = DirectoryNode(self.dir_path, ".", max_depth=max_depth)
        return project.get_content()
