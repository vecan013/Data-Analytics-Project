
from pathlib import Path
import csv
from getpass import getpass
import mysql.connector

PROJECT_DIR = Path(__file__).resolve().parent
CSV_FILE = PROJECT_DIR / "data" / "product_category_name_translation.csv"

conn = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password=getpass("MySQL root password: "),
    database="olist_analytics",
)

cursor = conn.cursor()

sql = """
INSERT INTO category_translation (
    product_category_name,
    product_category_name_english
) VALUES (%s, %s)
ON DUPLICATE KEY UPDATE
    product_category_name_english = VALUES(product_category_name_english)
"""

batch = []

with CSV_FILE.open("r", encoding="utf-8-sig", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        batch.append((
            row["product_category_name"],
            row["product_category_name_english"],
        ))

cursor.executemany(sql, batch)
conn.commit()

cursor.execute("SELECT COUNT(*) FROM category_translation")
print(f"Translation rows processed: {len(batch)}")
print(f"Rows currently in category_translation: {cursor.fetchone()[0]}")

cursor.close()
conn.close()
