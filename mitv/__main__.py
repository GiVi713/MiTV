"""Command-line entry point for MiTV."""

import argparse

from mitv import __version__


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="mitv", description="MiTV: начальная основа проекта."
    )
    parser.add_argument("--version", action="version", version=f"MiTV {__version__}")
    parser.parse_args()
    parser.print_help()


if __name__ == "__main__":
    main()
