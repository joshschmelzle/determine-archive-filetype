#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" determine common archive filetype's using magic bytes (file signature) """
__author__ = "Josh Schmelzle"
__version__ = "0.0.1"
__status__ = "Development"

import os
import sys
import argparse
import textwrap

if sys.version_info < (3, 2):
    print("python v3.2+ required")
    sys.exit(-1)


COMMON_MAGIC_BYTES = {
    "\x89\x50\x4e\x47\x0d\x0a\x1a\x0a": "png",
    "\x7b\x5c\x72\x74\x66\x31": "rtf",
    "\x4c\x5a\x49\x50": "lz",
    "\x37\x7a\xbc\xaf\x27\x1c": "7z",
    "\xfd\x37\x7a\x58\x5a\x00": "xz",
    "\x1f\x8b\x08": "gz",
    "\x42\x5a\x68": "bz2",
    "\x50\x4b\x03\x04": "zip",
}

MAX_LENGTH = max(len(x) for x in COMMON_MAGIC_BYTES)


def _setup_parser() -> argparse:
    """Setup parser for arguments passed in from the CLI.

    Returns:
      argparse object.
    """
    parser = argparse.ArgumentParser(
        description=textwrap.dedent(
            """
            Determine the file type for a few different kinds of files.
            It uses the magic bytes (file signature) to classify the file.
            This does not recurse into sub-folders.
            """
        ),
        epilog="Made with Python by {}".format(__author__),
        fromfile_prefix_chars="@",
    )

    parser.add_argument(
        "-V", "--version", action="version", version="%(prog)s {}".format(__version__)
    )

    parser.add_argument(
        "-f",
        "--file",
        nargs="?",
        dest="file",
        help="specific file to scan, can also be a folder",
    )

    parser.set_defaults()

    return parser


def is_likely_text(filename: str) -> bool:
    """ determine if file is likely just text

    python3 uses unicode when handling files in text mode.

    if the encoding can't handle an arbitrary file,
        then it's likely that `UnicodeDecodeError` will occur.
    """
    try:
        with open(filename, "r") as _file:
            for line in _file:
                pass
            return True
    except UnicodeDecodeError:
        return False  # Fond non-text data


def get_type(filename: str) -> str:
    """check input file's file signature against a few known magic bytes

        "Software should only work with Unicode strings internally,
        onverting to a particular encoding on output."

    https://docs.python.org/2.7/howto/unicode.html#the-unicode-type
    https://docs.python.org/2.7/howto/unicode.html
    """
    try:
        with open(filename, "rb") as file:
            byte = file.read(1)
            number = 1
            _bytes = bytearray()
            # print("{} byte {}".format(filename, byte))
            _bytes.append(ord(byte))
            while byte != b"":
                byte = file.read(1)
                # print("{} byte {}".format(filename, byte))
                _bytes.append(ord(byte))
                number = number + 1
                if number == MAX_LENGTH:
                    # print("{} bytes {}".format(filename, _bytes))
                    for magicbytes, filetype in COMMON_MAGIC_BYTES.items():
                        if _bytes.startswith(magicbytes.encode("latin-1", "ignore")):
                            return filetype
                    if is_likely_text(filename):
                        return "likely text"
                    return "no match"
    except PermissionError:
        return "no match (permission error)"


def main() -> None:
    arg_parser = _setup_parser()
    args = arg_parser.parse_args()

    if args.file:
        if os.path.isdir(args.file):
            for _file in os.listdir(os.getcwd()):
                try:
                    print("file: {}, type: {}".format(_file, get_type(_file)))
                except IsADirectoryError:
                    pass
        else:
            print("file: {}, type: {}".format(args.file, get_type(args.file)))


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("stop requested...")
        sys.exit(-1)
    sys.exit(0)
