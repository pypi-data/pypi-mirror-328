#!/usr/bin/env python3

import sys
from pathlib import Path

from .pyxelart_detector import is_pixel_art

def usage():
    print("Usage: pyxelart-detector <path/to/file.{png,jpg,gif,...}>")
    exit(1)

def main():
    if len(sys.argv) != 2:
        usage()

    filepath = Path(sys.argv[1])
    if not filepath.is_file():
        print(f"Error: {filepath} is not a valid file.")
        usage()

    print(is_pixel_art(filepath))

if __name__ == '__main__':
    main()
