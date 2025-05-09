import os

from path_pixie.common.exceptions import InvalidTags, PathNotFound
from path_pixie.saver.port import OutputSaver


class FileOutputSaver(OutputSaver):
    start_tag = "<!-- CONTENTS START -->"
    end_tag = "<!-- CONTENTS END -->"

    def __init__(self, filename: str, start_tag: str | None = None, end_tag: str | None = None):
        if not os.path.exists(filename):
            raise PathNotFound(f"File {filename} not found.")
        self.filename = filename
        self.start_tag = start_tag or self.start_tag
        self.end_tag = end_tag or self.end_tag

    def find_tags(self, content: str) -> tuple[int, int]:
        start = -1
        end = -1
        for line in content.splitlines():
            if line.startswith(self.start_tag):
                start = content.index(line) - 1
            if line.startswith(self.end_tag):
                end = content.index(line) + len(line)

        return start, end

    def __call__(self, output: str) -> None:
        with open(self.filename, "r") as f:
            content = f.read()
        start, end = self.find_tags(content)

        if start > end:
            raise InvalidTags("Start tag is greater than end tag.")

        no_tags = any((start < 0, end < 0))
        before = content if no_tags else content[:start]
        after = "" if no_tags else content[end:]

        output = f"\n{self.start_tag}\n" + output + f"\n{self.end_tag}"
        new_content = before + output + after

        with open(self.filename, "w") as f:
            f.write(new_content)
