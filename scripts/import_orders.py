
from pathlib import Path
import csv
import mysql.connector

PROJECT_DIR = Path(__file__).resolve().parent
CSV_FILE = PROJECT_DIR / "data" / "olist_orders_dataset.csv"

# Enter the MySQL root password when prompted.
from getpass import getpass
password = getpass("MySQL root password: ")

conn = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password=password,
    database="olist_analytics",
)
cursor = conn.cursor()

insert_sql = """
INSERT INTO orders (
    order_id,
    customer_id,
    order_status,
    order_purchase_timestamp,
    order_approved_at,
    order_delivered_carrier_date,
    order_delivered_customer_date,
    order_estimated_delivery_date
) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
"""

def clean(value):
    return value if value else None

inserted = 0

with CSV_FILE.open("r", encoding="utf-8-sig", newline="") as file:
    reader = csv.DictReader(file)
    batch = []

    for row in reader:
        batch.append((
            row["order_id"],
            row["customer_id"],
            row["order_status"],
            clean(row["order_purchase_timestamp"]),
            clean(row["order_approved_at"]),
            clean(row["order_delivered_carrier_date"]),
            clean(row["order_delivered_customer_date"]),
            clean(row["order_estimated_delivery_date"]),
        ))

        if len(batch) >= 1000:
            cursor.executemany(insert_sql, batch)
            conn.commit()
            inserted += len(batch)
            batch.clear()

    if batch:
        cursor.executemany(insert_sql, batch)
        conn.commit()
        inserted += len(batch)

print(f"Rows imported: {inserted}")

cursor.execute("SELECT COUNT(*) FROM orders")
print(f"Rows currently in orders: {cursor.fetchone()[0]}")

cursor.close()
conn.close()
