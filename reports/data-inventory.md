# Olist E-commerce Dataset Inventory

## 1. Project Overview

- Project Name: Olist E-commerce Sales & Customer Analytics
- Team Name: Zaalima
- Project Type: Data Analytics
- Objective: Analyze e-commerce sales, customer purchasing behavior, delivery performance, and customer satisfaction to identify useful business insights.

## 2. Dataset Source

The project uses the Olist Brazilian E-commerce dataset.

The dataset contains information about orders, customers, products, sellers, payments, reviews, geolocation, and product categories.

All nine original CSV files were checked locally using a Python verification script.

## 3. Dataset Inventory and Verification Results

| Dataset File | Rows | Columns | Missing Values | Duplicate Rows |
|---|---:|---:|---:|---:|
| olist_customers_dataset.csv | 99,441 | 5 | 0 | 0 |
| olist_geolocation_dataset.csv | 1,000,163 | 5 | 0 | 261,831 |
| olist_order_items_dataset.csv | 112,650 | 7 | 0 | 0 |
| olist_order_payments_dataset.csv | 103,886 | 5 | 0 | 0 |
| olist_order_reviews_dataset.csv | 99,224 | 7 | 145,903 | 0 |
| olist_orders_dataset.csv | 99,441 | 8 | 4,908 | 0 |
| olist_products_dataset.csv | 32,951 | 9 | 2,448 | 0 |
| olist_sellers_dataset.csv | 3,095 | 4 | 0 | 0 |
| product_category_name_translation.csv | 71 | 2 | 0 | 0 |

## 4. Dataset Descriptions

| Dataset File | Purpose |
|---|---|
| olist_orders_dataset.csv | Order identifiers, customer references, order status, and order dates |
| olist_customers_dataset.csv | Customer identifiers and customer location information |
| olist_order_items_dataset.csv | Products purchased, sellers, item prices, and freight charges |
| olist_order_payments_dataset.csv | Payment methods, installments, and payment values |
| olist_order_reviews_dataset.csv | Customer review scores, comments, and review timestamps |
| olist_products_dataset.csv | Product names, categories, dimensions, and weight |
| olist_sellers_dataset.csv | Seller identifiers and seller location information |
| olist_geolocation_dataset.csv | Geographic coordinates, postal-code prefixes, cities, and states |
| product_category_name_translation.csv | Portuguese product category names and their English translations |

## 5. Data Quality Findings

### 5.1 Customers

- Total records: 99,441
- Missing values: 0
- Duplicate rows: 0

No missing values or duplicate rows were detected.

### 5.2 Geolocation

- Total records: 1,000,163
- Missing values: 0
- Duplicate rows: 261,831

Duplicate rows were detected. These records should be considered during geographic analysis, and duplicates should not be removed without checking their effect on the analysis.

### 5.3 Order Items

- Total records: 112,650
- Missing values: 0
- Duplicate rows: 0

No missing values or duplicate rows were detected.

### 5.4 Payments

- Total records: 103,886
- Missing values: 0
- Duplicate rows: 0

No missing values or duplicate rows were detected.

### 5.5 Reviews

- Total records: 99,224
- Missing values: 145,903
- Duplicate rows: 0

Missing values by column:

| Column | Missing Values |
|---|---:|
| review_comment_title | 87,656 |
| review_comment_message | 58,247 |

The missing values are concentrated in review comment fields.

### 5.6 Orders

- Total records: 99,441
- Missing values: 4,908
- Duplicate rows: 0

Missing values by column:

| Column | Missing Values |
|---|---:|
| order_approved_at | 160 |
| order_delivered_carrier_date | 1,783 |
| order_delivered_customer_date | 2,965 |

Missing delivery timestamps must be considered when calculating delivery duration and delivery performance.

### 5.7 Products

- Total records: 32,951
- Missing values: 2,448
- Duplicate rows: 0

Missing values by column:

| Column | Missing Values |
|---|---:|
| product_category_name | 610 |
| product_name_lenght | 610 |
| product_description_lenght | 610 |
| product_photos_qty | 610 |
| product_weight_g | 2 |
| product_length_cm | 2 |
| product_height_cm | 2 |
| product_width_cm | 2 |

Missing product attributes should be handled appropriately before product-level analysis.

### 5.8 Sellers

- Total records: 3,095
- Missing values: 0
- Duplicate rows: 0

No missing values or duplicate rows were detected.

### 5.9 Category Translation

- Total records: 71
- Missing values: 0
- Duplicate rows: 0

No missing values or duplicate rows were detected.

## 6. Important Identifiers and Relationships

The following identifiers support dataset relationships:

- order_id: Connects orders with order items, payments, and reviews.
- customer_id: Connects orders with customer information.
- customer_unique_id: Identifies the same customer across multiple customer records.
- product_id: Connects order items with product information.
- seller_id: Connects order items with seller information.
- product_category_name: Connects products with category translations.

These relationships should be considered when joining datasets to avoid incorrect counts or duplicated sales values.

## 7. Planned Analysis Areas

### Sales Analysis
- Order volume and monthly trends.
- Sales value and average order value.
- Product and category performance.

### Customer Analysis
- Repeat and one-time customers.
- Order frequency.
- RFM customer segmentation.

### Delivery and Customer Satisfaction
- Delivery time and late-delivery rate.
- Review score distribution.
- Relationship between delivery performance and review scores.

## 8. Verification Method

Dataset verification was performed using Python and Pandas.

The verification script checked:

1. CSV file availability.
2. Total number of rows.
3. Total number of columns.
4. Actual column names.
5. Total missing values.
6. Duplicate rows.
7. Missing values in individual columns.

## 9. Conclusion

All nine Olist CSV datasets were successfully located and inspected.

The verification identified missing values in the orders, reviews, and products datasets, along with duplicate rows in the geolocation dataset.

These findings provide an initial understanding of the dataset structure and quality. Appropriate data cleaning and validation should be performed before using affected records in analysis.

**Status:** Initial dataset inventory and data-quality verification completed using the available local CSV files.