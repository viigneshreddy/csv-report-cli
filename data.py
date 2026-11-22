import shutil
from pathlib import Path

import kagglehub

path = Path(kagglehub.dataset_download("kyanyoga/sample-sales-data"))

data_dir = Path("/Users/viignesh/Downloads/Projects/csv-report-cli/Data")
data_dir.mkdir(parents=True, exist_ok=True)

for csv_file in path.glob("*.csv"):
    shutil.copy(csv_file, data_dir / csv_file.name)
    print("Copied:", data_dir / csv_file.name)