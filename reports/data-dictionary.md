# Olist E-commerce Data Dictionary

## 1. Purpose

This document describes the columns available in the Olist E-commerce dataset and explains their meanings and uses in the project.

All column names were checked against the original CSV files using Python and Pandas.

**Status:** Column names and dataset structures verified.

## 2. Orders Dataset

**File:** `olist_orders_dataset.csv`

| Column | Description |
|---|---|
| order_id | Unique identifier for an order |
| customer_id | Identifier linking an order to a customer |
| order_status | Current or recorded status of the order |
| order_purchase_timestamp | Date and time when the order was placed |
| order_approved_at | Date and time when the order was approved |
| order_delivered_carrier_date | Date and time when the order was handed to the carrier |
| order_delivered_customer_date | Date and time when the order was delivered to the customer |
| order_estimated_delivery_date | Estimated delivery date for the order |

**Dataset statistics:** 99,441 rows, 8 columns, 4,908 missing values, 0 duplicate rows.

## 3. Customers Dataset

**File:** `olist_customers_dataset.csv`

| Column | Description |
|---|---|
| customer_id | Identifier associated with a customer order record |
| customer_unique_id | Identifier used to recognize the same customer across orders |
| customer_zip_code_prefix | Customer's postal-code prefix |
| customer_city | Customer's city |
| customer_state | Customer's state |

**Dataset statistics:** 99,441 rows, 5 columns, 0 missing values, 0 duplicate rows.

## 4. Order Items Dataset

**File:** `olist_order_items_dataset.csv`

| Column | Description |
|---|---|
| order_id | Identifier of the order |
| order_item_id | Sequential item number within an order |
| product_id | Identifier of the product |
| seller_id | Identifier of the seller |
| shipping_limit_date | Deadline for the seller to hand the item to the carrier |
| price | Price of the order item |
| freight_value | Freight charge associated with the order item |

**Dataset statistics:** 112,650 rows, 7 columns, 0 missing values, 0 duplicate rows.

## 5. Payments Dataset

**File:** `olist_order_payments_dataset.csv`

| Column | Description |
|---|---|
| order_id | Identifier of the order |
| payment_sequential | Sequential number of a payment record for an order |
| payment_type | Payment method |
| payment_installments | Number of payment installments |
| payment_value | Value of the payment record |

**Dataset statistics:** 103,886 rows, 5 columns, 0 missing values, 0 duplicate rows.

## 6. Reviews Dataset

**File:** `olist_order_reviews_dataset.csv`

| Column | Description |
|---|---|
| review_id | Identifier of a review |
| order_id | Identifier of the reviewed order |
| review_score | Customer review score |
| review_comment_title | Title of the customer's review |
| review_comment_message | Text of the customer's review |
| review_creation_date | Date the review survey was created |
| review_answer_timestamp | Date and time the review was answered |

**Dataset statistics:** 99,224 rows, 7 columns, 145,903 missing values, 0 duplicate rows.

Missing values:

- review_comment_title: 87,656
- review_comment_message: 58,247

## 7. Products Dataset

**File:** `olist_products_dataset.csv`

| Column | Description |
|---|---|
| product_id | Unique identifier of a product |
| product_category_name | Product category name |
| product_name_lenght | Length of the product name |
| product_description_lenght | Length of the product description |
| product_photos_qty | Number of product photos |
| product_weight_g | Product weight in grams |
| product_length_cm | Product length in centimeters |
| product_height_cm | Product height in centimeters |
| product_width_cm | Product width in centimeters |

**Dataset statistics:** 32,951 rows, 9 columns, 2,448 missing values, 0 duplicate rows.

Missing values:

- product_category_name: 610
- product_name_lenght: 610
- product_description_lenght: 610
- product_photos_qty: 610
- product_weight_g: 2
- product_length_cm: 2
- product_height_cm: 2
- product_width_cm: 2

Note: The column spellings `product_name_lenght` and `product_description_lenght` are retained exactly as they appear in the original dataset.

## 8. Sellers Dataset

**File:** `olist_sellers_dataset.csv`

| Column | Description |
|---|---|
| seller_id | Unique identifier of a seller |
| seller_zip_code_prefix | Seller's postal-code prefix |
| seller_city | Seller's city |
| seller_state | Seller's state |

**Dataset statistics:** 3,095 rows, 4 columns, 0 missing values, 0 duplicate rows.

## 9. Geolocation Dataset

**File:** `olist_geolocation_dataset.csv`

| Column | Description |
|---|---|
| geolocation_zip_code_prefix | Postal-code prefix associated with the location |
| geolocation_lat | Geographic latitude |
| geolocation_lng | Geographic longitude |
| geolocation_city | City associated with the location |
| geolocation_state | State associated with the location |

**Dataset statistics:** 1,000,163 rows, 5 columns, 0 missing values, 261,831 duplicate rows.

Note: Duplicate rows were detected during verification. Their treatment should depend on the requirements of the geographic analysis.

## 10. Product Category Translation Dataset

**File:** `product_category_name_translation.csv`

| Column | Description |
|---|---|
| product_category_name | Original Portuguese product category name |
| product_category_name_english | English translation of the product category name |

**Dataset statistics:** 71 rows, 2 columns, 0 missing values, 0 duplicate rows.

## 11. Important Dataset Relationships

The following relationships support the project's analysis:

| Relationship | Join Column |
|---|---|
| Orders and Customers | customer_id |
| Orders and Order Items | order_id |
| Orders and Payments | order_id |
| Orders and Reviews | order_id |
| Order Items and Products | product_id |
| Order Items and Sellers | seller_id |
| Products and Category Translation | product_category_name |

Important considerations:

- An order can contain multiple order-item records.
- An order can contain multiple payment records.
- Review records should be checked before joining to orders.
- Geolocation may contain multiple records for a postal-code prefix.
- Aggregate order-item and payment values appropriately before joining to avoid double-counting.

## 12. Data Quality Considerations

The verification identified the following:

1. The orders dataset contains missing approval and delivery timestamps.
2. The reviews dataset contains missing review titles and messages.
3. The products dataset contains missing category and product attribute values.
4. The geolocation dataset contains duplicate rows.
5. The remaining datasets have no missing values or duplicate rows according to the verification script.

Missing values and duplicates should be handled according to the requirements of each analysis. Original CSV files should remain unchanged.

## 13. Conclusion

The data dictionary documents all nine Olist CSV datasets and their verified column names.

It provides a reference for understanding the dataset structure, identifying important fields, and establishing relationships between tables.

**Status:** Initial data dictionary completed and column names verified against the original CSV files.