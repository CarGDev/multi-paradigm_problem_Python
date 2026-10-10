from utils.validate_data import ColumnType

from .quartiles_percentiles import QuartilesPercentiles
from .variance import Variance


class Statistics:
    def __init__(self, list_data):
        self.list = list_data
        self._quartiles = QuartilesPercentiles(list_data)
        self._variance = Variance(list_data)

    def summatory(self) -> float:
        total = 0.0
        for v in self.list.values:
            total += v
        print(f"Sum: {total:f}")
        return total

    def mean(self) -> None:
        total = self.summatory()
        print(f"Mean: {total / self.list.count:f}")

    def _runs(self) -> list[tuple[float, int]]:
        vals = self.list.values
        runs: list[tuple[float, int]] = []
        i = 0
        n = len(vals)
        while i < n:
            j = i
            while j < n and vals[j] == vals[i]:
                j += 1
            runs.append((vals[i], j - i))
            i = j
        return runs

    def mode(self) -> None:
        if self.list.count == 0:
            return
        runs = self._runs()
        max_run = max([1] + [length for _, length in runs])
        if max_run == 1:
            print("Mode: there is no mode")
            return
        out = "Mode:"
        for value, length in runs:
            if length == max_run:
                if self.list.type == ColumnType.INT:
                    out += f" {int(value)}"
                else:
                    out += f" {float(value):f}"
        print(out)

    def median(self) -> None:
        n = self.list.count
        if n == 0:
            return
        vals = self.list.values
        if n % 2 != 0:
            m = vals[n // 2]
            if self.list.type == ColumnType.INT:
                print(f"Median: {m}")
            else:
                print(f"Median: {m:f}")
        else:
            avg = (vals[n // 2 - 1] + vals[n // 2]) / 2.0
            print(f"Median: {avg:f}")

    def quartiles(self) -> None:
        self._quartiles.quartiles()

    def variance(self) -> None:
        self._variance.variance()
