import sys

from core import CreatingResults, CsvReader
from tui import Menu


class App:
    def __init__(self, argv: list[str]):
        self.argv = argv

    def run(self) -> int:
        headers = CsvReader(self.argv).csv_headers()
        if not headers:
            print("statistics: no data", file=sys.stderr)
            return 1

        option = Menu(headers).menu()
        if option < 0:
            print("statistics: no numeric column selected", file=sys.stderr)
            return 1

        CreatingResults(headers, option, self.argv).run()
        return 0


def main() -> None:
    sys.exit(App(sys.argv).run())


if __name__ == "__main__":
    main()
