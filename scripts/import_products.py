
from pathlib import Path
import csv
from getpass import getpass
import mysql.connector

PROJECT_DIR = Path(__file__).resolve().parent
CSV_FILE = PROJECT_DIR / "data" / "olist_products_dataset.csv"

conn = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password=getpass("MySQL root password: "),
    database="olist_analytics",
)
cursor = conn.cursor()

sql = """
INSERT INTO products (
    product_id, product_category_name, product_name_length,
    product_description_length, product_photos_qty,
    product_weight_g, product_length_cm, product_height_cm,
    product_width_cm
) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
ON DUPLICATE KEY UPDATE
    product_category_name = VALUES(product_category_name),
    product_name_length = VALUES(product_name_length),
    product_description_length = VALUES(product_description_length),
    product_photos_qty = VALUES(product_photos_qty),
    product_weight_g = VALUES(product_weight_g),
    product_length_cm = VALUES(product_length_cm),
    product_height_cm = VALUES(product_height_cm),
    product_width_cm = VALUES(product_width_cm)
"""

def to_int(value):
    return int(value) if value else None

batch = []
processed = 0

with CSV_FILE.open("r", encoding="utf-8-sig", newline="") as f:
    for row in csv.DictReader(f):
        batch.append((
            row["product_id"],
            row["product_category_name"] or None,
            to_int(row["product_name_lenght"]),
            to_int(row["product_description_lenght"]),
            to_int(row["product_photos_qty"]),
            to_int(row["product_weight_g"]),
            to_int(row["product_length_cm"]),
            to_int(row["product_height_cm"]),
            to_int(row["product_width_cm"]),
        ))

        if len(batch) >= 1000:
            cursor.executemany(sql, batch)
            conn.commit()
            processed += len(batch)
            batch.clear()

    if batch:
        cursor.executemany(sql, batch)
        conn.commit()
        processed += len(batch)

cursor.execute("SELECT COUNT(*) FROM products")
print(f"CSV rows processed: {processed}")
print(f"Rows currently in products: {cursor.fetchone()[0]}")

cursor.close()
conn.close()
