from pathlib import Path
import pandas as pd
import csv

def generate_report(csv_path: Path) -> str:
    df = pd.read_csv(csv_path, encoding='latin-1')
    return f"Report generated for {csv_path.name} with {len(df)} rows."

with open('sales_data_sample.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=['Date', 'Product', 'Quantity', 'Price'])


if __name__ == "__main__":
    # Example usage
    report = generate_report(Path("/Users/viignesh/Downloads/Projects/csv-report-cli/data/sales_data_sample.csv"))
    print(report)