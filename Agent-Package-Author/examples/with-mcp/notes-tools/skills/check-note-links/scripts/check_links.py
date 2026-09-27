"""Report missing local Markdown link targets in one note."""

import argparse
from pathlib import Path
import re


def main() -> int:
    """Print missing relative targets without following network links."""
    parser = argparse.ArgumentParser()
    parser.add_argument('path', type=Path)
    path = parser.parse_args().path
    for target in re.findall(r'\]\(([^)]+)\)', path.read_text(encoding='utf-8')):
        if '://' not in target and not (path.parent / target.split('#')[0]).exists():
            print('missing: ' + target)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
