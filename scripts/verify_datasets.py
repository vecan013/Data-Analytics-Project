
import pandas as pd
from pathlib import Path

# Project data folder
DATA_DIR = Path("data")

csv_files = list(DATA_DIR.rglob("*.csv"))

if not csv_files:
    print("No CSV files found. Check your data folder.")
    exit()

print("\nOLIST DATASET VERIFICATION")
print("=" * 70)

for file in sorted(csv_files):
    try:
        df = pd.read_csv(file)

        print(f"\nDataset: {file.name}")
        print(f"Rows: {len(df):,}")
        print(f"Columns: {len(df.columns)}")
        print(f"Column names: {', '.join(df.columns)}")
        print(f"Missing values: {df.isnull().sum().sum():,}")
        print(f"Duplicate rows: {df.duplicated().sum():,}")

        missing = df.isnull().sum()
        missing = missing[missing > 0]

        if not missing.empty:
            print("Missing values by column:")
            print(missing.to_string())

    except Exception as e:
        print(f"\nError reading {file.name}: {e}")

print("\n" + "=" * 70)
print("DATASET VERIFICATION COMPLETED")
