
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

PROJECT_DIR = Path(__file__).resolve().parent.parent
OUTPUT_DIR = PROJECT_DIR / "output"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Chart 1: Monthly item sales
monthly = pd.read_csv(OUTPUT_DIR / "monthly_sales.csv")

plt.figure(figsize=(12, 6))
plt.plot(
    monthly["month"],
    monthly["item_sales_value"],
    marker="o"
)
plt.title("Monthly Item Sales Value")
plt.xlabel("Purchase Month")
plt.ylabel("Item Sales Value")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "monthly_sales.png", dpi=150)
plt.close()

# Chart 2: Top product categories
categories = pd.read_csv(OUTPUT_DIR / "top_product_categories.csv")
categories = categories.sort_values("item_sales_value")

plt.figure(figsize=(10, 6))
plt.barh(categories["category"], categories["item_sales_value"])
plt.title("Top 10 Product Categories by Item Sales Value")
plt.xlabel("Item Sales Value")
plt.ylabel("Product Category")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "top_product_categories.png", dpi=150)
plt.close()

print("Charts saved:")
print(OUTPUT_DIR / "monthly_sales.png")
print(OUTPUT_DIR / "top_product_categories.png")
