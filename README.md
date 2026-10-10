# multi-paradigm_problem_Python

Command-line program written in Python (object-oriented style) that reads a CSV file, lets you pick one numeric column, and prints descriptive statistics for it. It is the Python part of a multi-paradigm assignment (C, OCaml, Python) that computes mean, median and mode.

## Setup

```sh
python3 -m venv .venv
```

There are no external dependencies, only the Python standard library.

## Run

```sh
make run CSV=./test.csv
```

This runs `.venv/bin/python src/main.py ./test.csv`. The CSV must be comma-separated with a header row. The program lists the numeric columns of the file:

```text
Select one option to return data:

1: task_id
2: worker_id
...
15: fare
16: duration_ms

Choose an option:
```

Type the number of a column and press Enter.

## What to expect

For the chosen column the program prints the statistics of its values, sorted internally:

```text
Median: 17.930000
Sum: 366136.940000
Mean: 18.306847
Mode: 7.580000
Q1: 12.380000
Q2: 17.930000
Q3: 23.740000
IQR: 11.360000
Population variance: 56.380645
Population std dev: 7.508705
Sample variance: 56.383464
Sample std dev: 7.508892
Min: 2.580000
Max: 42.060000
Range: 39.480000
```

- Integer columns (e.g. `task_id`) are handled as integers, decimal columns (e.g. `fare`) as decimals.
- Median of an even count is the average of the two middle values.
- Mode prints every most frequent value (all of them when there is a tie); if every value is unique it reports that there is no mode.
- Quartiles use linear interpolation between ranks; IQR is Q3 - Q1.

## Project structure

```text
src/
  main.py                          App class, entry point
  core/data.py                     CsvReader: finds the numeric columns
  core/order_data.py               CreatingResults: loads, sorts (heap sort) and prints the results
  tui/menu.py                      Menu: asks which column to analyze
  utils/delimiter.py               Delimiter: splits a CSV line (handles quotes)
  utils/validate_data.py           Validator: tells if a cell is an integer, decimal or invalid
  statistic/main.py                Statistics: sum, mean, median, mode
  statistic/quartiles_percentiles.py   QuartilesPercentiles: Q1, Q2, Q3, IQR
  statistic/variance.py            Variance: population and sample variance and std dev
```
