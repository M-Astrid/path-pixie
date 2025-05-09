from typing import Any

from path_pixie.common.const import DEFAULT_DEPTH
from path_pixie.renderer.port import Renderer
from path_pixie.tree.port import LeafContent


class MDListRenderer(Renderer):
    ident: str = "  "
    prefix_template: str = "{ident}{char} "
    link_template: str = "[{name}]({link})"
    base_template: str = "{name}"
    dir_char = "-"
    file_char = "-"
    end_char = "  \n"
    output = ""

    def __call__(self, content: LeafContent, depth: int = DEFAULT_DEPTH, is_links: bool = False, **kwargs: Any) -> str:
        self.output += self.prefix_template.format(char=self.file_char, ident=self.ident * content.depth)
        if is_links:
            self.output += self.link_template.format(name=content.name, link=content.full_path)
        else:
            self.output += self.base_template.format(name=content.name)

        self.output += self.end_char

        for child in content.children:
            self(child, is_links=is_links)

        return self.output


class HTMLRenderer(Renderer):
    def __call__(self, content: LeafContent, depth: int = DEFAULT_DEPTH, **kwargs: Any) -> str:
        raise NotImplementedError


class TextRenderer(Renderer):
    prefix_template: str = "{'  '*depth}{char} "
    ident_char: str = "  "
    end_char = "  \n"

    def __call__(self, content: LeafContent, depth: int = DEFAULT_DEPTH, is_links: bool = False, **kwargs: Any) -> str:
        # content = leaf.get_content()
        # output = self.prefix_template.format(char="└─" if content.depth == 0
        # else "├─", ident=content.depth*self.ident_char)
        raise NotImplementedError
