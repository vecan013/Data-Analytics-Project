
from pathlib import Path
import pandas as pd

# Project folders
PROJECT_DIR = Path(__file__).resolve().parent
DATA_DIR = PROJECT_DIR / "data"

# Dataset paths
orders_file = DATA_DIR / "olist_orders_dataset.csv"
reviews_file = DATA_DIR / "olist_order_reviews_dataset.csv"

# Check whether the files exist
print("Orders file exists:", orders_file.exists())
print("Reviews file exists:", reviews_file.exists())

# Load datasets
orders = pd.read_csv(orders_file)
reviews = pd.read_csv(reviews_file)

# Inspect the datasets
print("\nORDERS DATASET")
print("Shape:", orders.shape)
print("Columns:", orders.columns.tolist())
print(orders.head())

print("\nREVIEWS DATASET")
print("Shape:", reviews.shape)
print("Columns:", reviews.columns.tolist())
print(reviews.head())

# Check dataset quality
print("\n--- ORDERS DATA QUALITY ---")
print("Missing values:")
print(orders.isnull().sum())

print("\nDuplicate order IDs:", orders["order_id"].duplicated().sum())
print("Order status counts:")
print(orders["order_status"].value_counts(dropna=False))

print("\n--- REVIEWS DATA QUALITY ---")
print("Missing values:")
print(reviews.isnull().sum())

print("\nDuplicate review IDs:", reviews["review_id"].duplicated().sum())
print("Duplicate review-order pairs:",
      reviews.duplicated(subset=["order_id"]).sum())

# Convert date columns to datetime
date_columns = [
    "order_purchase_timestamp",
    "order_delivered_customer_date",
    "order_estimated_delivery_date"
]

for column in date_columns:
    orders[column] = pd.to_datetime(orders[column], errors="coerce")

reviews["review_creation_date"] = pd.to_datetime(
    reviews["review_creation_date"], errors="coerce"
)

print("\nDate columns converted successfully.")
print(orders[date_columns].dtypes)

# ==========================================
# DELIVERY PERFORMANCE ANALYSIS
# ==========================================

# Keep only delivered orders for delivery analysis
delivered = orders[
    orders["order_status"].eq("delivered")
].copy()

# Calculate delivery duration in days
delivered["delivery_time_days"] = (
    delivered["order_delivered_customer_date"]
    - delivered["order_purchase_timestamp"]
).dt.total_seconds() / (24 * 60 * 60)

# Identify orders with valid delivery durations
valid_delivery = delivered[
    delivered["order_purchase_timestamp"].notna()
    & delivered["order_delivered_customer_date"].notna()
    & delivered["delivery_time_days"].ge(0)
].copy()

# Count delivered orders excluded from duration calculations
excluded_delivery_orders = len(delivered) - len(valid_delivery)

print("\n--- DELIVERY TIME METRICS ---")
print("Total delivered orders:", len(delivered))
print("Valid delivery records:", len(valid_delivery))
print("Orders excluded due to missing/invalid dates:",
      excluded_delivery_orders)

if not valid_delivery.empty:
    print("Average delivery time (days):",
          round(valid_delivery["delivery_time_days"].mean(), 2))
    print("Median delivery time (days):",
          round(valid_delivery["delivery_time_days"].median(), 2))
    print("Minimum delivery time (days):",
          round(valid_delivery["delivery_time_days"].min(), 2))
    print("Maximum delivery time (days):",
          round(valid_delivery["delivery_time_days"].max(), 2))

# ==========================================
# ON-TIME AND LATE DELIVERY ANALYSIS
# ==========================================

eligible = valid_delivery[
    valid_delivery["order_estimated_delivery_date"].notna()
].copy()

eligible["delivery_status"] = (
    eligible["order_delivered_customer_date"]
    > eligible["order_estimated_delivery_date"]
).map({True: "Late", False: "On-time"})

late_count = (eligible["delivery_status"] == "Late").sum()
on_time_count = (eligible["delivery_status"] == "On-time").sum()
eligible_count = len(eligible)

late_rate = (
    late_count / eligible_count * 100
    if eligible_count else 0
)
on_time_rate = (
    on_time_count / eligible_count * 100
    if eligible_count else 0
)

print("\n--- DELIVERY PERFORMANCE ---")
print("Eligible delivered orders:", eligible_count)
print("Late orders:", late_count)
print("On-time orders:", on_time_count)
print("Late delivery rate (%):", round(late_rate, 2))
print("On-time delivery rate (%):", round(on_time_rate, 2))

# ==========================================
# SAVE DELIVERY SUMMARY
# ==========================================

OUTPUT_DIR = PROJECT_DIR / "output"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

delivery_summary = pd.DataFrame({
    "metric": [
        "Total delivered orders",
        "Valid delivery records",
        "Excluded delivery records",
        "Average delivery time (days)",
        "Median delivery time (days)",
        "Minimum delivery time (days)",
        "Maximum delivery time (days)",
        "Eligible delivered orders",
        "Late orders",
        "On-time orders",
        "Late delivery rate (%)",
        "On-time delivery rate (%)"
    ],
    "value": [
        len(delivered),
        len(valid_delivery),
        excluded_delivery_orders,
        valid_delivery["delivery_time_days"].mean()
            if not valid_delivery.empty else None,
        valid_delivery["delivery_time_days"].median()
            if not valid_delivery.empty else None,
        valid_delivery["delivery_time_days"].min()
            if not valid_delivery.empty else None,
        valid_delivery["delivery_time_days"].max()
            if not valid_delivery.empty else None,
        eligible_count,
        late_count,
        on_time_count,
        late_rate,
        on_time_rate
    ]
})

delivery_summary.to_csv(
    OUTPUT_DIR / "delivery_summary.csv", index=False
)

print("\nDelivery summary saved to output/delivery_summary.csv")

# ==========================================
# CUSTOMER SATISFACTION ANALYSIS
# ==========================================

# Keep one review record per order for this comparison.
# If an order has multiple reviews, use the average score.
review_scores = (
    reviews.groupby("order_id", as_index=False)
    .agg(review_score=("review_score", "mean"))
)


# Investigate eligible orders without matching review records
eligible_order_ids = set(eligible["order_id"].dropna().unique())
review_order_ids = set(reviews["order_id"].dropna().unique())

missing_review_ids = eligible_order_ids - review_order_ids

print("\n--- REVIEW MATCH INVESTIGATION ---")
print("Eligible delivered orders:", len(eligible_order_ids))
print("Unique orders with review records:", len(review_order_ids))
print("Eligible orders with matching reviews:",
      len(eligible_order_ids & review_order_ids))
print("Eligible orders without review records:",
      len(missing_review_ids))

print("\nSample eligible orders without reviews:")
print(list(missing_review_ids)[:10])

# Check matched reviews with missing review scores
matched_review_data = eligible[["order_id"]].merge(
    review_scores,
    on="order_id",
    how="inner",
    validate="one_to_one"
)

print("\nMatched orders with missing review scores:",
      matched_review_data["review_score"].isna().sum())
print("Matched orders with valid review scores:",
      matched_review_data["review_score"].notna().sum())

# Merge review scores with delivery status
satisfaction = eligible.merge(
    review_scores,
    on="order_id",
    how="inner",
    validate="one_to_one"
).dropna(subset=["review_score"])

print("\n--- CUSTOMER SATISFACTION ---")
print("Delivered orders matched with reviews:", len(satisfaction))

if not satisfaction.empty:
    satisfaction_summary = (
        satisfaction.groupby("delivery_status")
        .agg(
            orders=("order_id", "count"),
            average_review_score=("review_score", "mean"),
            median_review_score=("review_score", "median")
        )
        .round(2)
    )

    print("\nReview scores by delivery status:")
    print(satisfaction_summary)

    # Save satisfaction results
    satisfaction_summary.to_csv(
        OUTPUT_DIR / "customer_satisfaction_summary.csv"
    )

    print(
        "\nCustomer satisfaction summary saved to "
        "output/customer_satisfaction_summary.csv"
    )
else:
    print("No matching review records were found.")

# ==========================================
# DATA VISUALIZATION
# ==========================================

import matplotlib.pyplot as plt
import seaborn as sns

CHART_DIR = OUTPUT_DIR / "charts"
CHART_DIR.mkdir(parents=True, exist_ok=True)

sns.set_theme(style="whitegrid")

# Chart 1: On-time vs late delivery rates
delivery_labels = ["On-time", "Late"]
delivery_values = [on_time_rate, late_rate]

plt.figure(figsize=(8, 5))
ax = sns.barplot(
    x=delivery_labels,
    y=delivery_values
)
ax.set_title("On-Time vs Late Delivery Rate")
ax.set_xlabel("Delivery Status")
ax.set_ylabel("Percentage of Eligible Orders (%)")
ax.bar_label(ax.containers[0], fmt="%.2f%%")
plt.tight_layout()
plt.savefig(
    CHART_DIR / "delivery_performance.png",
    dpi=300,
    bbox_inches="tight"
)
plt.close()

# Chart 2: Average review score by delivery status
review_plot = (
    satisfaction.groupby("delivery_status")["review_score"]
    .mean()
    .reindex(["On-time", "Late"])
    .dropna()
)

plt.figure(figsize=(8, 5))
ax = sns.barplot(
    x=review_plot.index,
    y=review_plot.values
)
ax.set_title("Average Customer Review Score by Delivery Status")
ax.set_xlabel("Delivery Status")
ax.set_ylabel("Average Review Score (out of 5)")
ax.set_ylim(0, 5)
ax.bar_label(ax.containers[0], fmt="%.2f")
plt.tight_layout()
plt.savefig(
    CHART_DIR / "customer_satisfaction.png",
    dpi=300,
    bbox_inches="tight"
)
plt.close()

# Chart 3: Distribution of delivery duration
plt.figure(figsize=(9, 5))
sns.histplot(
    data=valid_delivery,
    x="delivery_time_days",
    bins=50
)
plt.title("Distribution of Delivery Time")
plt.xlabel("Delivery Time (days)")
plt.ylabel("Number of Orders")
plt.tight_layout()
plt.savefig(
    CHART_DIR / "delivery_time_distribution.png",
    dpi=300,
    bbox_inches="tight"
)
plt.close()

print("\nCharts saved in output/charts/")
