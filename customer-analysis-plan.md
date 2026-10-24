# Customer Purchasing Behavior Analysis Plan

## 1. Objective

The objective of this analysis is to understand customer purchasing behavior in the Olist E-commerce dataset.

The analysis will focus on identifying unique customers, measuring repeat purchases, examining customer locations, analyzing purchasing patterns, calculating order values, and performing RFM (Recency, Frequency, Monetary) customer segmentation.

The final results will help identify valuable customer groups, understand purchasing trends, and suggest data-driven improvements to customer retention and marketing strategies.

## 2. Business Questions

The analysis will answer the following questions:

1. How many unique customers are represented in the dataset?
2. How many customers make repeat purchases?
3. What percentage of customers are repeat customers?
4. Which states and cities have the highest numbers of customers?
5. How many orders are placed each month?
6. What is the average number of orders per customer?
7. Which product categories appear most frequently in orders?
8. What is the average order value (AOV)?
9. Which customers have purchased most recently, most frequently, or spent the most?
10. What customer segments can be identified using RFM analysis?

## 3. Required Datasets

The following CSV files will be used.

| Dataset | Purpose |
|---|---|
| `olist_customers_dataset.csv` | Customer identifiers and location |
| `olist_orders_dataset.csv` | Order identifiers, customer mapping, order status, and purchase dates |
| `olist_order_items_dataset.csv` | Product items, product prices, freight charges, and order-item details |
| `olist_products_dataset.csv` | Product information and category names |
| `product_category_name_translation.csv` | English translations of product categories, when available |

Only the datasets required for each analysis will be loaded.

### Important Columns

**Customers dataset**
- `customer_id`
- `customer_unique_id`
- `customer_city`
- `customer_state`
- `customer_zip_code_prefix`

**Orders dataset**
- `order_id`
- `customer_id`
- `order_status`
- `order_purchase_timestamp`

**Order items dataset**
- `order_id`
- `order_item_id`
- `product_id`
- `price`
- `freight_value`

**Products dataset**
- `product_id`
- `product_category_name`

## 4. Table Relationships

The datasets will be connected using the following relationships:

1. Customers and orders: join using `customer_id`.
2. Orders and order items: join using `order_id`.
3. Order items and products: join using `product_id`.
4. Products and category translations: join using `product_category_name`.

The joins will be validated to avoid unintended duplicate records and incorrect customer or order counts.

## 5. Customer Identifier Definitions

### `customer_id`

Identifies a customer record associated with an order. It is used to connect the customers dataset to the orders dataset.

### `customer_unique_id`

Represents the same underlying customer across potentially multiple customer records. It is used to count unique customers and identify repeat purchasing behavior.

### Analysis Rule

Customer-level metrics will use `customer_unique_id`, while joins between customers and orders will use `customer_id`.

Distinct customer counts will be calculated from customers who have at least one eligible order, unless a metric explicitly states otherwise.

## 6. Repeat Customer Analysis

A repeat customer is defined as a unique customer who has placed more than one eligible order during the available observation period.

### Methodology

1. Load the customers and orders datasets.
2. Review order statuses and document which orders qualify for purchasing analysis.
3. Join customers to orders using `customer_id`.
4. Group the eligible orders by `customer_unique_id`.
5. Count distinct `order_id` values for each unique customer.
6. Classify customers with more than one eligible order as repeat customers.
7. Classify customers with exactly one eligible order as one-time customers.
8. Calculate the repeat customer rate.

### Metrics

| Metric | Definition |
|---|---|
| Unique Customers | Number of distinct `customer_unique_id` values with eligible orders |
| Repeat Customers | Number of unique customers with more than one eligible order |
| One-Time Customers | Number of unique customers with exactly one eligible order |
| Repeat Customer Rate | Repeat customers divided by all eligible unique customers, multiplied by 100 |
| Average Orders per Customer | Total distinct eligible orders divided by eligible unique customers |

Cancelled orders and other excluded statuses will be documented. The chosen eligibility rules will be applied consistently.

## 7. Customer Location Analysis

Customer location analysis will examine the geographic distribution of customers using the city and state recorded in the customers dataset.

### Business Questions

- Which states have the most unique customers?
- Which cities have the most unique customers?
- What percentage of customers belong to each state?
- How are eligible orders distributed across states?

### Metrics

- Unique customers by state.
- Unique customers by city.
- Eligible orders by state.
- Percentage of unique customers by state.

Customer counts will use distinct `customer_unique_id` values rather than the number of customer records.

Customer location represents the location recorded in the dataset and may not reflect the customer's current residence or the actual delivery destination.

## 8. Purchasing-Pattern Analysis

This section will examine purchasing frequency, order volumes, and product-category patterns.

### A. Monthly Order Trends

Methodology:

1. Convert `order_purchase_timestamp` to datetime format.
2. Apply the documented order eligibility rules.
3. Group eligible orders by purchase month.
4. Count distinct orders in each month.
5. Plot the monthly order-volume trend.

Metric:

Monthly Order Volume = Number of distinct eligible orders purchased during each month.

### B. Product-Category Analysis

Methodology:

1. Join orders with order items using `order_id`.
2. Join order items with products using `product_id`.
3. Translate category names into English when a translation is available.
4. Rank categories using clearly defined measures.

Metrics may include:

- Number of distinct orders containing each category.
- Number of product items sold by category.
- Total product sales value by category.

Category rankings will specify which metric is being used. Orders containing multiple products will not be incorrectly counted as multiple distinct orders.

### C. Average Order Value (AOV)

Average Order Value measures the average monetary value of an eligible order.

For this project, AOV will use product prices plus freight charges unless the team explicitly adopts a different definition.

Methodology:

1. Aggregate product prices and freight charges by `order_id`.
2. Calculate the total value of each eligible order.
3. Calculate the average across eligible orders.

Formula:

AOV = Total value of eligible orders divided by the number of eligible orders.

Each order will be counted once, even if it contains multiple items.

## 9. RFM Customer Segmentation

RFM stands for Recency, Frequency, and Monetary value. It will be used to group customers according to their purchasing behavior.

### RFM Metrics

| Component | Definition | Required Data |
|---|---|---|
| Recency | Number of days between a customer's latest eligible purchase and the reference date | `customer_unique_id`, `order_purchase_timestamp` |
| Frequency | Number of distinct eligible orders placed by a customer | `customer_unique_id`, `order_id` |
| Monetary | Total value of eligible orders associated with a customer | `customer_unique_id`, `order_id`, `price`, `freight_value` |

### Methodology

1. Select the eligible order population.
2. Determine the latest purchase date for each unique customer.
3. Define and document a common reference date for Recency calculations.
4. Count distinct eligible orders for Frequency.
5. Aggregate order values by customer for Monetary.
6. Assign RFM scores using a consistent, documented scoring method.
7. Combine the scores to create interpretable customer segments.
8. Summarize the size and characteristics of each segment.

Potential segments include recent customers, frequent customers, high-spending customers, loyal customers, and customers who may benefit from re-engagement.

These are possible segment labels, not confirmed findings. Final labels and scoring thresholds will be determined after inspecting the data.

## 10. Data Cleaning and Quality Checks

The following checks will be performed before analysis:

1. Inspect dataset dimensions, column names, and data types.
2. Check missing values and duplicate records.
3. Validate key identifiers such as `customer_id`, `customer_unique_id`, and `order_id`.
4. Convert purchase timestamps to datetime format.
5. Check for invalid or missing purchase timestamps.
6. Document the treatment of canceled, unavailable, and other excluded orders.
7. Check that joins do not unintentionally multiply customer or order records.
8. Validate that each eligible order is counted only once in order-level metrics.
9. Check for missing product categories and category translations.
10. Confirm that the final calculations use the intended eligible population.

Any important data-quality issues and exclusions will be documented in the notebook.

## 11. Suggested Visualizations

The following visualizations will be created:

1. KPI cards showing unique customers, repeat customer rate, and average order value.
2. Bar chart showing repeat customers versus one-time customers.
3. Bar chart showing the top customer states.
4. Bar chart showing the top customer cities.
5. Line chart showing monthly order volume.
6. Bar chart showing the most frequently purchased product categories.
7. Bar chart showing customer counts across RFM segments.

Charts will have meaningful titles, labeled axes, and appropriate units.

## 12. Implementation Requirements

Create a Jupyter notebook named:

`customer_purchasing_behavior_analysis.ipynb`

The notebook must contain:

1. Project objective and business questions.
2. Library imports and dataset loading.
3. Data inspection and quality checks.
4. Data cleaning and preparation.
5. Customer identifier analysis.
6. Repeat and one-time customer calculations.
7. Customer location analysis.
8. Monthly purchasing trends.
9. Product-category analysis.
10. Average order value calculation.
11. RFM calculations and segmentation.
12. Visualizations.
13. Key findings and business recommendations.

Use Python, Pandas, Matplotlib, and Seaborn if needed.

The notebook must contain executable code and actual results, not only descriptions of intended analysis.

## 13. Final Findings Document

Create a Markdown file named:

`customer-analysis-findings.md`

Include:

- Project objective.
- Summary of unique and repeat customers.
- Repeat customer rate and average orders per customer.
- Important customer location patterns.
- Monthly order-volume trends.
- Product-category findings.
- Average order value.
- RFM segment summaries.
- Three to five evidence-based business recommendations.
- Data limitations and assumptions.

All numerical findings must come from the actual analysis. Do not invent customer counts, percentages, trends, or segment results.

## 14. Definition of Done

The task will be considered complete when:

- The analysis plan is reviewed and approved.
- The required datasets are inspected and cleaned.
- Repeat customer metrics are calculated and validated.
- Customer location and purchasing patterns are analyzed.
- Average order value is calculated using the documented definition.
- RFM metrics and customer segments are produced.
- The required visualizations are generated.
- The findings document contains actual results and recommendations.
- The notebook runs successfully from beginning to end.
- The final files are committed to GitHub and submitted through a pull request.

## 15. Scope and Deadline

The project deadline is 8 November 2026.

Prioritize the core analysis first:

1. Unique and repeat customer analysis.
2. Customer location analysis.
3. Monthly order-volume analysis.
4. Average order value and product-category analysis.
5. RFM segmentation.
6. Findings and recommendations.

If time becomes limited, complete the core calculations and main visualizations before adding optional details.

**Current status:** Planning and implementation pending.
