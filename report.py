from pathlib import Path

import pandas as pd


class SalesReport:
    def __init__(self, csv_path: Path):
        self.csv_path = csv_path
        self.df = pd.read_csv(csv_path, encoding="latin-1")  # read once

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