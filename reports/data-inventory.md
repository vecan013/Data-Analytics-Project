# Olist E-commerce Dataset Inventory

## 1. Project Overview

- **Project Name:** Olist E-commerce Sales & Customer Analytics
- **Team Name:** Zaalima
- **Project Type:** Data Analytics
- **Objective:** Analyze e-commerce sales, customer purchasing behavior, delivery performance, and customer satisfaction to identify useful business insights.

## 2. Dataset Source

The project uses the Olist Brazilian E-Commerce dataset.

The dataset contains information about orders, customers, products, sellers, payments, reviews, and delivery.

**Note:** The availability of each CSV file must be verified in our local dataset folder.

## 3. Dataset Files

| Dataset File | Purpose | Status |
|---|---|---|
| `olist_orders_dataset.csv` | Order status and order dates | To verify |
| `olist_customers_dataset.csv` | Customer IDs and location | To verify |
| `olist_order_items_dataset.csv` | Products, prices, freight, and order items | To verify |
| `olist_order_payments_dataset.csv` | Payment types and payment values | To verify |
| `olist_order_reviews_dataset.csv` | Customer review scores and comments | To verify |
| `olist_products_dataset.csv` | Product details and categories | To verify |
| `olist_sellers_dataset.csv` | Seller identifiers and location | To verify |
| `olist_geolocation_dataset.csv` | Geographic coordinates and postal codes | To verify |
| `product_category_name_translation.csv` | English translations of product categories | To verify |

## 4. Important Identifiers and Relationships

The following identifiers are expected to be useful for joining the datasets:

- `order_id`: Connects order information with order items, payments, and reviews.
- `customer_id`: Connects orders with customer information.
- `customer_unique_id`: Helps identify the same customer across multiple orders.
- `product_id`: Connects order items with product information.
- `seller_id`: Connects order items with seller information.

These relationships must be validated against the actual CSV files before analysis.

## 5. Planned Data Quality Checks

The team will perform the following checks:

1. Identify missing values in important columns.
2. Check duplicate records and identifiers.
3. Validate dates, numeric values, and data types.
4. Check for invalid or inconsistent order statuses.
5. Verify relationships between datasets.
6. Check whether multiple rows per order are expected in item, payment, or review data.
7. Document any data limitations that may affect the results.

## 6. Planned Analysis Areas

### Sales Analysis
- Order volume and monthly trends
- Sales value and average order value
- Product and category performance

### Customer Analysis
- Repeat and one-time customers
- Order frequency
- RFM customer segmentation

### Delivery and Customer Satisfaction
- Delivery time and late-delivery rate
- Review score distribution
- Relationship between delivery performance and review scores

## 7. Pending Tasks

- [ ] Verify the CSV files available locally.
- [ ] Record the row and column counts of each file.
- [ ] Document the columns and their meanings.
- [ ] Complete missing-value and duplicate checks.
- [ ] Validate dataset relationships and join keys.
- [ ] Update this inventory with verified findings.

## 8. Conclusion

This inventory provides the initial structure for understanding the datasets used in the Olist E-commerce Analytics project. It will be updated as the team verifies the source files and completes data quality checks.

**Important:** Dataset counts, missing-value results, and other statistical findings will be added only after inspecting the actual data.
