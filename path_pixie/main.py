from path_pixie.common.const import DEFAULT_DEPTH
from path_pixie.renderer.adapter.renderer import MDListRenderer, TextRenderer
from path_pixie.saver.adapter.file import FileOutputSaver
from path_pixie.tree.adapter.composite import Project

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Cute directory tree generator.")

    parser.add_argument(
        "--format", type=str, default="md", choices=["md", "txt"], help="Формат вывода: текст или markdown."
    )
    parser.add_argument("--depth", type=int, default=DEFAULT_DEPTH, help="Максимальная глубина обхода.")
    parser.add_argument("--output", type=str, default=None, help="Имя файла для вывода результата.")

    args = parser.parse_known_args()[0]

    depth, format_ = args.depth, args.format

    render = MDListRenderer() if format_ == "md" else TextRenderer()
    project = Project("knowledge_base")
    tree = project.get_content(max_depth=depth)

    formatted = render(tree, is_links=True, depth=depth)

    if args.output:
        FileOutputSaver("readme.md")(formatted)
    else:
        print(formatted)
