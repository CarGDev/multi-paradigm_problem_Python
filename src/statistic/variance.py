import math


class Variance:
    def __init__(self, list_data):
        self.list = list_data

    def variance(self) -> None:
        n = self.list.count
        if n == 0:
            return
        vals = [float(v) for v in self.list.values]

        total = 0.0
        for v in vals:
            total += v
        avg = total / n

        squares = 0.0
        for v in vals:
            d = v - avg
            squares += d * d

        population = squares / n
        print(f"Population variance: {population:f}")
        print(f"Population std dev: {math.sqrt(population):f}")

        if n < 2:
            print("Sample variance: needs at least 2 values")
            return
        sample = squares / (n - 1)
        print(f"Sample variance: {sample:f}")
        print(f"Sample std dev: {math.sqrt(sample):f}")
