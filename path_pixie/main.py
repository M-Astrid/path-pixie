import argparse

from path_pixie import TreeBuilder
from path_pixie.common.const import DEFAULT_DEPTH

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Cute directory tree generator.")

    parser.add_argument("--depth", type=int, default=DEFAULT_DEPTH, help="Максимальная глубина обхода.")
    parser.add_argument("--output", type=str, default=None, help="Имя файла для вывода результата.")
    parser.add_argument("--root", type=str, default=".", help="Путь к корневой директории.")
    parser.add_argument("--is_links", type=bool, default=True, help="Ссылки вместо обычных текстовых имен.")

    args = parser.parse_known_args()[0]

    TreeBuilder()(
        dir_path=args.root,
        depth=args.depth,
        output=args.output,
        dir_links=args.is_links,
        file_links=args.is_links,
        prefix=args.prefix,
    )
