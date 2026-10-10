from core.data import Header


class Menu:
    def __init__(self, headers: list[Header]):
        self.headers = headers

    def menu(self) -> int:
        total = len(self.headers)
        if total == 0:
            return -1

        print("Select one option to return data:\n")
        for i, h in enumerate(self.headers):
            print(f"{i + 1}: {h.name}")

        while True:
            print("\nChoose an option: ", end="", flush=True)
            buffer = input_line()
            if buffer is None:
                return -1
            try:
                value = int(buffer.strip(), 10)
            except ValueError:
                value = None
            if value is not None and 1 <= value <= total:
                return value - 1
            print(f"Invalid option, enter a number between 1 and {total}.")


def input_line() -> str | None:
    import sys

    line = sys.stdin.readline()
    return line if line != "" else None
