# Delivery Performance & Customer Satisfaction Analysis

## 1. Objective

The objective of this analysis is to evaluate delivery performance in the Olist e-commerce platform and investigate how delivery delays relate to customer satisfaction. We will calculate delivery KPIs, analyze customer review scores, identify monthly trends, and recommend improvements based on the results.

## 2. Business Questions

1. What is the average delivery time?
2. How many orders were delivered on time and how many were late?
3. What is the on-time delivery rate?
4. What is the average customer review score?
5. Do late deliveries tend to receive lower review scores?
6. Which months have better or worse delivery performance?
7. What improvements could help Olist improve delivery performance and customer satisfaction?

## 3. Dataset Files

The following Olist CSV files will be used:

- `olist_orders_dataset.csv`
- `olist_order_reviews_dataset.csv`

The order items dataset is optional and should only be used if additional analysis requires it.

### Important Columns

**Orders dataset**
- `order_id`
- `order_status`
- `order_purchase_timestamp`
- `order_delivered_customer_date`
- `order_estimated_delivery_date`

**Reviews dataset**
- `review_id`
- `order_id`
- `review_score`
- `review_creation_date`
- `review_answer_timestamp`

## 4. Key Metrics and Definitions

| Metric | Definition |
|---|---|
| Average Delivery Time | Average days between purchase timestamp and actual customer delivery timestamp |
| On-Time Orders | Delivered orders where actual delivery date is on or before the estimated delivery date |
| Late Orders | Delivered orders where actual delivery date is after the estimated delivery date |
| On-Time Delivery Rate | On-time orders divided by eligible delivered orders, multiplied by 100 |
| Late Delivery Rate | Late orders divided by eligible delivered orders, multiplied by 100 |
| Average Review Score | Mean of available customer review scores |
| Review Score by Delivery Status | Average review score for on-time and late orders |
| Monthly Delivery Performance | Monthly on-time rate, late delivery rate, and average delivery time |

## 5. Data Preparation and Quality Checks

1. Load the required CSV files using Pandas.
2. Inspect the number of rows, columns, data types, and sample records.
3. Check for missing values and duplicate records.
4. Convert relevant timestamp columns to datetime format.
5. Use delivered orders with valid purchase and delivery timestamps for delivery-time calculations.
6. Exclude canceled, unavailable, and undelivered orders from delivery performance calculations.
7. Classify eligible delivered orders as on-time or late by comparing actual and estimated delivery dates.
8. Check whether review records contain multiple entries for the same order.
9. Aggregate review scores to one order-level value before joining with orders if multiple reviews exist.
10. Validate the final dataset to ensure that joining reviews does not unintentionally duplicate orders.

## 6. Analysis Methodology

### A. Delivery Performance

- Calculate delivery time in days.
- Calculate average delivery time.
- Count on-time and late orders.
- Calculate on-time and late delivery rates.
- Identify the proportion of eligible orders that were delivered after their estimated dates.

### B. Customer Satisfaction

- Calculate the average review score.
- Count reviews for each score from 1 to 5.
- Calculate average review scores for on-time and late orders.
- Compare review score distributions between the two delivery groups.

### C. Monthly Trends

- Group orders by purchase month.
- Calculate monthly delivery performance metrics.
- Compare on-time and late delivery rates across months.
- Mention that purchase-month grouping measures the performance of orders purchased during each month, not necessarily orders delivered during that month.

### D. Findings and
