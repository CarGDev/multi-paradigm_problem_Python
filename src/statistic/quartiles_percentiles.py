import math


class QuartilesPercentiles:
    def __init__(self, list_data):
        self.list = list_data

    def percentile(self, p: float) -> float:
        n = self.list.count
        if n == 0:
            return 0.0
        rank = p / 100.0 * (n - 1)
        lo = math.floor(rank)
        hi = lo + 1 if lo + 1 < n else lo
        frac = rank - lo
        a = float(self.list.values[lo])
        b = float(self.list.values[hi])
        return a + frac * (b - a)

    def quartiles(self) -> None:
        if self.list.count == 0:
            return
        q1 = self.percentile(25)
        q2 = self.percentile(50)
        q3 = self.percentile(75)
        print(f"Q1: {q1:f}")
        print(f"Q2: {q2:f}")
        print(f"Q3: {q3:f}")
        print(f"IQR: {q3 - q1:f}")
