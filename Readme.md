# csv-report-cli

A small command-line tool that reads a sales CSV and prints a summary report: row count, total sales, average order value, and top product line.

## Example output

```
Sales report: sales_data_sample.csv
Rows: 2,823
Total sales: $10,032,628.85
Avg order value: $32,677.94
Top product line: Classic Cars
```

## Requirements

- Python 3.10+
- pandas
- pytest (for running tests)

## Setup

```bash
git clone <repo-url>
cd csv-report-cli
python -m venv .venv
source .venv/bin/activate
pip install pandas pytest
```

## Usage

```bash
python main.py path/to/sales.csv
```

Or use it from Python:

```python
from main import SalesReport, generate_report

print(generate_report("sales.csv"))

report = SalesReport("sales.csv")
report.total_sales()       # float
report.avg_order_value()   # float
report.top_product_line()  # str
```

## Input format

The CSV must contain these columns:

| Column        | Description                        |
|---------------|------------------------------------|
| `SALES`       | Sale amount for the row (numeric)  |
| `ORDERNUMBER` | Order ID, used for avg order value |
| `PRODUCTLINE` | Product category                   |

Files are read with `latin-1` encoding.

## How it handles bad data

- **Missing file** – raises `FileNotFoundError`
- **Empty file or header only** – raises `ValueError("CSV has no data rows")`
- **Non-numeric `SALES` values** – those rows are skipped and a warning is printed to stderr
- **Average order value** – total sales divided by the number of *unique* order numbers, not by row count

## Running tests

From the project root:

```bash
python -m pytest
```

## Project structure

```
csv-report-cli/
├── main.py              # SalesReport class and generate_report()
├── tests/
│   └── test_report.py   # pytest suite
└── README.md
```