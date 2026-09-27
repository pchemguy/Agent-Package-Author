"""Count whitespace-delimited words in a command-line string."""

import argparse


def main() -> int:
    """Print the count for the supplied text."""
    parser = argparse.ArgumentParser()
    parser.add_argument('text')
    print(len(parser.parse_args().text.split()))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
