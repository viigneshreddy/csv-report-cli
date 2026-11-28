import sys
from pathlib import Path

import pandas as pd


class SalesReport:
    def __init__(self, csv_path: Path):
        self.csv_path = Path(csv_path)
        if not self.csv_path.is_file():
            raise FileNotFoundError(f"File not found: {self.csv_path}")

        try:
            df = pd.read_csv(self.csv_path, encoding="latin-1")
        except pd.errors.EmptyDataError:
            raise ValueError("CSV has no data rows")

        df["SALES"] = pd.to_numeric(df["SALES"], errors="coerce")
        bad = int(df["SALES"].isna().sum())
        if bad:
            print(f"Warning: skipped {bad} row(s) with invalid SALES values", file=sys.stderr)
            df = df.dropna(subset=["SALES"])

        if df.empty:
            raise ValueError("CSV has no data rows")

        self.df = df

    def row_count(self) -> int:
        return len(self.df)

    def total_sales(self) -> float:
        return float(self.df["SALES"].sum())

    def avg_order_value(self) -> float:
        return self.total_sales() / self.df["ORDERNUMBER"].nunique()

    def top_product_line(self) -> str:
        return self.df.groupby("PRODUCTLINE")["SALES"].sum().idxmax()

    def summary(self) -> str:
        return "\n".join([
            f"Sales report: {self.csv_path.name}",
            f"Rows: {self.row_count():,}",
            f"Total sales: ${self.total_sales():,.2f}",
            f"Avg order value: ${self.avg_order_value():,.2f}",
            f"Top product line: {self.top_product_line()}",
        ])


def generate_report(csv_path: Path) -> str:
    return SalesReport(csv_path).summary()