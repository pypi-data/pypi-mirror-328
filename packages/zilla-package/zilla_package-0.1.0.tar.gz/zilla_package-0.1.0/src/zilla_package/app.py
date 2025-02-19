import argparse

from _version import __version__
from zilla_package.zilla import Zilla


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Zilla-Package: a simple package."
    )

    parser.add_argument("--name", type=str, help="name of the zilla")
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")

    args = parser.parse_args()
    name = args.name
    zilla = Zilla.create(name)
    print(zilla)
