import sys
from dataclasses import dataclass, field

from statistic import Statistics
from utils.delimiter import Delimiter
from utils.validate_data import ColumnType, Validator

from .data import Header


@dataclass
class ValuesData:
    type: ColumnType
    values: list = field(default_factory=list)

    @property
    def count(self) -> int:
        return len(self.values)


class CreatingResults:
    def __init__(self, headers: list[Header], option: int, argv: list[str]):
        self.headers = headers
        self.option = option
        self.argv = argv

    def getting_all_data(self) -> ValuesData:
        try:
            fp = open(self.argv[1], "r", newline="")
        except OSError as e:
            print(f"fopen: {e.strerror}", file=sys.stderr)
            sys.exit(1)

        header = self.headers[self.option]
        values = ValuesData(header.type)
        parse = (
            Validator.parse_int if header.type == ColumnType.INT else Validator.parse_double
        )

        with fp:
            fp.readline()
            for row in fp:
                tokens = Delimiter.str_split(row, ",")
                if tokens is None:
                    break
                if header.index < len(tokens):
                    v = parse(tokens[header.index])
                    if v is not None:
                        values.values.append(v)
        return values

    @staticmethod
    def heaping(arr: list, n: int, i: int) -> None:
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n and arr[l] > arr[largest]:
            largest = l
        if r < n and arr[r] > arr[largest]:
            largest = r

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            CreatingResults.heaping(arr, n, largest)

    @staticmethod
    def sorting(data: ValuesData) -> None:
        arr = data.values
        n = len(arr)
        for i in range(n // 2 - 1, -1, -1):
            CreatingResults.heaping(arr, n, i)
        for i in range(n - 1, 0, -1):
            arr[0], arr[i] = arr[i], arr[0]
            CreatingResults.heaping(arr, i, 0)

    def order(self) -> ValuesData:
        data = self.getting_all_data()
        self.sorting(data)
        return data

    def run(self) -> None:
        data = self.order()
        if data.count == 0:
            print("statistics: the column has no valid values", file=sys.stderr)
            return
        stats = Statistics(data)
        stats.median()
        stats.mean()
        stats.mode()
        stats.quartiles()
        stats.variance()
        lo = data.values[0]
        hi = data.values[-1]
        rng = float(hi - lo)
        if data.type == ColumnType.INT:
            print(f"Min: {lo}")
            print(f"Max: {hi}")
        else:
            print(f"Min: {lo:f}")
            print(f"Max: {hi:f}")
        print(f"Range: {rng:f}")
