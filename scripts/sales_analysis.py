from pathlib import Path
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_DIR / "data"
OUTPUT_DIR = PROJECT_DIR / "output"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

orders = pd.read_csv(DATA_DIR / "olist_orders_dataset.csv")
items = pd.read_csv(DATA_DIR / "olist_order_items_dataset.csv")
products = pd.read_csv(DATA_DIR / "olist_products_dataset.csv")
translation = pd.read_csv(
    DATA_DIR / "product_category_name_translation.csv"
)

# Use delivered orders for this initial sales analysis.
delivered_orders = orders.loc[
    orders["order_status"].eq("delivered"),
    ["order_id", "order_purchase_timestamp"]
].copy()

items["price"] = pd.to_numeric(items["price"], errors="coerce")
delivered_items = items.merge(
    delivered_orders,
    on="order_id",
    how="inner",
    validate="many_to_one"
)

total_orders = delivered_orders["order_id"].nunique()
total_sales = delivered_items["price"].sum()
average_order_value = (
    total_sales / total_orders if total_orders else 0
)

print("\n=== SALES KPI SUMMARY ===")
print(f"Delivered orders: {total_orders:,}")
print(f"Item sales value: {total_sales:,.2f}")
print(f"Average item sales value per delivered order: {average_order_value:,.2f}")

# Monthly item sales based on purchase month.
delivered_items["order_purchase_timestamp"] = pd.to_datetime(
    delivered_items["order_purchase_timestamp"],
    errors="coerce"
)

delivered_items["month"] = (
    delivered_items["order_purchase_timestamp"].dt.to_period("M").astype(str)
)

monthly_sales = (
    delivered_items.dropna(subset=["month"])
    .groupby("month", as_index=False)["price"]
    .sum()
    .rename(columns={"price": "item_sales_value"})
)

monthly_sales.to_csv(
    OUTPUT_DIR / "monthly_sales.csv",
    index=False
)

# Product category performance.
category_data = delivered_items.merge(
    products[["product_id", "product_category_name"]],
    on="product_id",
    how="left",
    validate="many_to_one"
)

category_data = category_data.merge(
    translation,
    on="product_category_name",
    how="left",
    validate="many_to_one"
)

category_column = "product_category_name_english"
category_data[category_column] = category_data[category_column].fillna(
    category_data["product_category_name"]
).fillna("Unknown")

top_categories = (
    category_data.groupby(category_column, as_index=False)["price"]
    .sum()
    .sort_values("price", ascending=False)
    .head(10)
    .rename(columns={
        category_column: "category",
        "price": "item_sales_value"
    })
)

top_categories.to_csv(
    OUTPUT_DIR / "top_product_categories.csv",
    index=False
)

print("\nTop 10 product categories by item sales value:")
print(top_categories.to_string(index=False))

print("\nSaved reports:")
print(OUTPUT_DIR / "monthly_sales.csv")
print(OUTPUT_DIR / "top_product_categories.csv")
