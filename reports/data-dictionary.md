# Olist E-commerce Data Dictionary

## 1. Purpose

This document describes important columns in the Olist E-commerce dataset and explains how they may be used in the project.

**Status:** Initial draft. Column names and meanings must be checked against the actual CSV files before analysis.

## 2. Orders Dataset

**File:** `olist_orders_dataset.csv`

| Column | Expected meaning | Verification status |
|---|---|---|
| `order_id` | Unique identifier for an order | To verify |
| `customer_id` | Identifier linking an order to a customer | To verify |
| `order_status` | Current or recorded status of the order | To verify |
| `order_purchase_timestamp` | Date and time the order was placed | To verify |
| `order_approved_at` | Date and time the order was approved | To verify |
| `order_delivered_customer_date` | Date and time the order was delivered to the customer | To verify |
| `order_estimated_delivery_date` | Estimated delivery date | To verify |

## 3. Customers Dataset

**File:** `olist_customers_dataset.csv`

| Column | Expected meaning | Verification status |
|---|---|---|
| `customer_id` | Identifier associated with a customer order record | To verify |
| `customer_unique_id` | Identifier used to recognize the same customer across orders | To verify |
| `customer_city` | Customer's city | To verify |
| `customer_state` | Customer's state | To verify |
| `customer_zip_code_prefix` | Customer's postal-code prefix | To verify |

## 4. Order Items Dataset

**File:** `olist_order_items_dataset.csv`

| Column | Expected meaning | Verification status |
|---|---|---|
| `order_id` | Identifier of the order | To verify |
| `order_item_id` | Sequential item number within an order | To verify |
| `product_id` | Identifier of the product | To verify |
| `seller_id` | Identifier of the seller | To verify |
| `price` | Price of the order item | To verify |
| `freight_value` | Freight charge associated with the order item | To verify |

## 5. Payments Dataset

**File:** `olist_order_payments_dataset.csv`

| Column | Expected meaning | Verification status |
|---|---|---|
| `order_id` | Identifier of the order | To verify |
| `payment_sequential` | Sequential number of a payment method for an order | To verify |
| `payment_type` | Payment method | To verify |
| `payment_installments` | Number of payment installments | To verify |
| `payment_value` | Value of the payment record | To verify |

## 6. Reviews Dataset

**File:** `olist_order_reviews_dataset.csv`

| Column | Expected meaning | Verification status |
|---|---|---|
| `review_id` | Identifier of a review | To verify |
| `order_id` | Identifier of the reviewed order | To verify |
| `review_score` | Customer review score | To verify |
| `review_creation_date` | Date the review survey was created | To verify |
| `review_answer_timestamp` | Date and time the review was answered | To verify |

## 7. Planned Dataset Relationships

The following relationships are expected to support the analysis:

- Orders and customers: `customer_id`
- Orders and order items: `order_id`
- Orders and payments: `order_id`
- Orders and reviews: `order_id`
- Order items and products: `product_id`
- Order items and sellers: `seller_id`

These relationships must be validated before joining datasets. Some datasets may contain multiple records for a single order.

## 
