
from pathlib import Path
import csv
from getpass import getpass
import mysql.connector

PROJECT_DIR = Path(__file__).resolve().parent
CSV_FILE = PROJECT_DIR / "data" / "olist_order_items_dataset.csv"

conn = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password=getpass("MySQL root password: "),
    database="olist_analytics",
)

cursor = conn.cursor()
sql = """
INSERT INTO order_items (
    order_id, order_item_id, product_id, seller_id,
    shipping_limit_date, price, freight_value
) VALUES (%s, %s, %s, %s, %s, %s, %s)
ON DUPLICATE KEY UPDATE
    product_id = VALUES(product_id),
    seller_id = VALUES(seller_id),
    shipping_limit_date = VALUES(shipping_limit_date),
    price = VALUES(price),
    freight_value = VALUES(freight_value)
"""

count = 0
batch = []

with CSV_FILE.open("r", encoding="utf-8-sig", newline="") as f:
    for row in csv.DictReader(f):
        batch.append((
            row["order_id"],
            int(row["order_item_id"]),
            row["product_id"] or None,
            row["seller_id"] or None,
            row["shipping_limit_date"] or None,
            row["price"] or None,
            row["freight_value"] or None,
        ))

        if len(batch) >= 1000:
            cursor.executemany(sql, batch)
            conn.commit()
            count += len(batch)
            batch.clear()

    if batch:
        cursor.executemany(sql, batch)
        conn.commit()
        count += len(batch)

cursor.execute("SELECT COUNT(*) FROM order_items")
print(f"CSV rows processed: {count}")
print(f"Rows currently in order_items: {cursor.fetchone()[0]}")

cursor.close()
conn.close()
