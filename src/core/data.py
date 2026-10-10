import sys
from dataclasses import dataclass

from utils.delimiter import Delimiter
from utils.validate_data import ColumnType, Validator


@dataclass
class Header:
    name: str
    index: int
    type: ColumnType


class CsvReader:
    def __init__(self, argv: list[str]):
        self.argv = argv

    def csv_headers(self) -> list[Header] | None:
        if len(self.argv) != 2:
            print("Only one argument is allowed", file=sys.stderr, end="")
            sys.exit(1)
        try:
            fp = open(self.argv[1], "r", newline="")
        except OSError:
            print("statictics: Invalid file.", file=sys.stderr)
            sys.exit(1)

        with fp:
            prev_headers = fp.readline()
            line = fp.readline()
        if prev_headers == "" or line == "":
            return None

        tokens = Delimiter.str_split(prev_headers, ",")
        tokens_lines = Delimiter.str_split(line, ",")
        if tokens is None or tokens_lines is None:
            print("statistics: out of memory", file=sys.stderr)
            sys.exit(1)

        headers: list[Header] = []
        for i, name in enumerate(tokens):
            valid = (
                Validator.validate_data(tokens_lines[i])
                if i < len(tokens_lines)
                else ColumnType.INVALID
            )
            if valid != ColumnType.INVALID:
                headers.append(Header(name, i, valid))
        return headers
