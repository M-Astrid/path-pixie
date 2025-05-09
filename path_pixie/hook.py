import argparse

from path_pixie.common.const import DEFAULT_DEPTH
from path_pixie.renderer.adapter.renderer import MDListRenderer
from path_pixie.saver.adapter.file import FileOutputSaver
from path_pixie.tree.adapter.composite import Project


def run() -> None:
    parser = argparse.ArgumentParser(description="Cute directory tree generator.")

    parser.add_argument("--depth", type=int, default=DEFAULT_DEPTH, help="Максимальная глубина обхода.")
    parser.add_argument("--output", type=str, default="readme.md", help="Имя файла для вывода результата.")
    parser.add_argument("--root", type=str, default=".", help="Путь к корневой директории.")
    parser.add_argument("--is_links", type=bool, default=True, help="Ссылки вместо обычных текстовых имен.")

    args = parser.parse_known_args()[0]

    depth, output, root = args.depth, args.output, args.root

    render = MDListRenderer()
    project = Project(root)
    tree = project.get_content(max_depth=depth)

    formatted = render(tree, is_links=args.is_links, depth=depth)
    FileOutputSaver(output)(formatted)
