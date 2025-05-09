from typing import Any

from path_pixie.common.const import DEFAULT_DEPTH
from path_pixie.common.exceptions import UnknownPrefix
from path_pixie.renderer.adapter.mdlist.enums import Prefix
from path_pixie.renderer.port import Renderer
from path_pixie.tree.port import NodeInfo


class MDListRenderer(Renderer):
    ident: str = "  "
    dir_char = "-"
    file_char = "-"
    end_char = "  \n"
    output = ""
    __prefix_template: str = "{ident}{char} "
    __link_template: str = "[{name}]({link})"
    __base_template: str = "{name}"
    __signoff_template: str = "*{text}*  \n"

    def __init__(
        self,
        prefix_type: Prefix = Prefix.bullet,
        ident: str = ident,
        end_char: str = end_char,
        dir_char: str = None,
        file_char: str = None,
    ):
        self.set_prefix_chars(prefix_type)
        self.dir_char = dir_char or self.dir_char
        self.file_char = file_char or self.file_char
        self.ident = ident
        self.end_char = end_char

    def set_prefix_chars(self, prefix_type: str) -> None:
        match prefix_type:
            case Prefix.emoji:
                self.dir_char = "- :file_folder:"
                self.file_char = "- :page_facing_up:"
            case Prefix.bullet:
                self.dir_char = "-"
                self.file_char = "-"
            case Prefix.number:
                self.dir_char = "1."
                self.file_char = "1."
            case _:
                raise UnknownPrefix(f"Prefix type {prefix_type} not found. Allowed types: {", ".join(Prefix)}")

    def __render(self, content: NodeInfo, depth: int = DEFAULT_DEPTH, is_links: bool = False) -> str:
        self.output += self.__prefix_template.format(
            char=self.dir_char if content.is_dir else self.file_char, ident=self.ident * content.depth
        )

        if is_links:
            self.output += self.__link_template.format(name=content.name, link=content.full_path)
        else:
            self.output += self.__base_template.format(name=content.name)

        self.output += self.end_char

        for child in content.children:
            self(child, is_links=is_links)

        return self.output

    def __call__(
        self, content: NodeInfo, depth: int = DEFAULT_DEPTH, is_links: bool = False, signoff: str = "", **kwargs: Any
    ) -> str:
        self.output += self.__signoff_template.format(text=signoff) if signoff else ""
        return self.__render(content, depth=depth, is_links=is_links)
