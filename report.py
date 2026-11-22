from pathlib import Path
import pandas as pd

def generate_report(csv_path: Path) -> str:
    df = pd.read_csv(csv_path)
    return f"Report generated for {csv_path.name} with {len(df)} rows."