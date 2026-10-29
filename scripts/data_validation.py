from pathlib import Path
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_DIR / "data"
OUTPUT_DIR = PROJECT_DIR / "output"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

results = []

for csv_file in sorted(DATA_DIR.glob("*.csv")):
    print(f"\nChecking: {csv_file.name}")

    try:
        df = pd.read_csv(csv_file)

        result = {
            "dataset": csv_file.name,
            "rows": len(df),
            "columns": len(df.columns),
            "missing_values": int(df.isna().sum().sum()),
            "duplicate_rows": int(df.duplicated().sum()),
            "column_names": ", ".join(df.columns),
            "status": "Success",
        }

        print(f"Rows: {result['rows']:,}")
        print(f"Columns: {result['columns']}")
        print(f"Missing values: {result['missing_values']:,}")
        print(f"Duplicate rows: {result['duplicate_rows']:,}")

    except Exception as error:
        result = {
            "dataset": csv_file.name,
            "rows": None,
            "columns": None,
            "missing_values": None,
            "duplicate_rows": None,
            "column_names": "",
            "status": f"Error: {error}",
        }
        print(result["status"])

    results.append(result)

report = pd.DataFrame(results)
report_path = OUTPUT_DIR / "data_quality_summary.csv"
report.to_csv(report_path, index=False)

print(f"\nReport saved to: {report_path}")
print("Data validation completed.")
