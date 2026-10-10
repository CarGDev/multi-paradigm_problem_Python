from enum import Enum


class ColumnType(Enum):
    INT = 0
    DOUBLE = 1
    INVALID = 2


class Validator:

    @staticmethod
    def parse_int(text: str) -> int | None:
        if text == "" or "_" in text or text != text.rstrip():
            return None
        try:
            return int(text, 10)
        except ValueError:
            return None

    @staticmethod
    def parse_double(text: str) -> float | None:
        if text == "" or "_" in text or text != text.rstrip():
            return None
        try:
            return float(text)
        except ValueError:
            return None

    @classmethod
    def validate_data(cls, val: str | None) -> ColumnType:
        if val is None or val == "":
            return ColumnType.INVALID
        if cls.parse_int(val) is not None:
            return ColumnType.INT
        if cls.parse_double(val) is not None:
            return ColumnType.DOUBLE
        return ColumnType.INVALID
