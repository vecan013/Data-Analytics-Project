
from pathlib import Path
import csv
from getpass import getpass
import mysql.connector

PROJECT_DIR = Path(__file__).resolve().parent
CSV_FILE = PROJECT_DIR / "data" / "olist_order_payments_dataset.csv"

conn = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password=getpass("MySQL root password: "),
    database="olist_analytics",
)

cursor = conn.cursor()

sql = """
INSERT INTO payments (
    order_id, payment_sequential, payment_type,
    payment_installments, payment_value
) VALUES (%s, %s, %s, %s, %s)
ON DUPLICATE KEY UPDATE
    payment_type = VALUES(payment_type),
    payment_installments = VALUES(payment_installments),
    payment_value = VALUES(payment_value)
"""

batch = []
processed = 0

with CSV_FILE.open("r", encoding="utf-8-sig", newline="") as f:
    for row in csv.DictReader(f):
        batch.append((
            row["order_id"],
            int(row["payment_sequential"]),
            row["payment_type"] or None,
            int(row["payment_installments"]) if row["payment_installments"] else None,
            row["payment_value"] or None,
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

cursor.execute("SELECT COUNT(*) FROM payments")
print(f"CSV rows processed: {processed}")
print(f"Rows currently in payments: {cursor.fetchone()[0]}")

cursor.close()
conn.close()
