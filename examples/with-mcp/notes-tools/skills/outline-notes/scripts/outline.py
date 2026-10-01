"""List Markdown heading text as an outline."""

import argparse
from pathlib import Path


def main() -> int:
    """Read a Markdown path and print headings in their original order."""
    parser = argparse.ArgumentParser()
    parser.add_argument('path', type=Path)
    for line in parser.parse_args().path.read_text(encoding='utf-8').splitlines():
        if line.startswith('#') and line.lstrip('#').startswith(' '):
            print('- ' + line.lstrip('#').strip())
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
