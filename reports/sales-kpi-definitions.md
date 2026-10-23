# Sales KPI Definitions

## 1. Project Overview

**Project:** Olist E-commerce Sales & Customer Analytics  
**Team:** Zaalima

## 2. Purpose

This document defines the key performance indicators (KPIs) that the team will use to analyze sales performance in the Olist Brazilian E-Commerce dataset.

The actual KPI values will be calculated after validating the source data.

## 3. Data Sources

The expected datasets are:

- `olist_orders_dataset.csv`
- `olist_order_items_dataset.csv`
- `olist_order_payments_dataset.csv`
- `olist_products_dataset.csv`
- `product_category_name_translation.csv`

The team must verify that these files and their required columns are available before performing the calculations.

## 4. Key Performance Indicators

### KPI 1: Total Orders

**Definition:** Number of distinct orders included in the analysis.

**Calculation:** Count distinct `order_id` values from the selected order population.

**Business value:** Helps measure order volume and purchasing activity.

### KPI 2: Total Item Sales Value

**Definition:** Sum of item prices for the selected orders.

**Calculation:** Sum the `price` column in `olist_order_items_dataset.csv`.

**Business value:** Helps evaluate sales performance over time and across products.

**Note:** Item sales value is not necessarily equal to total customer payments. Freight, cancellations, refunds, and payment adjustments must be considered separately where relevant.

### KPI 3: Average Order Value (AOV)

**Definition:** Average item sales value per distinct included order.

**Calculation:**

Average Order Value = Total Item Sales Value / Number of Distinct Included Orders

**Business value:** Helps measure the average item value associated with an order.

**Note:** The numerator and denominator must use the same order population.

### KPI 4: Monthly Sales Trend

**Definition:** Total item sales value grouped by calendar month.

**Calculation:** Group the selected order-item sales by the chosen order date and sum `price` for each month.

**Business value:** Helps identify seasonal patterns, increases, and decreases in sales.

### KPI 5: Monthly Order Trend

**Definition:** Number of distinct orders per calendar month.

**Calculation:** Group orders by purchase month and count distinct `order_id` values.

**Business value:** Shows how order volume changes over time.

### KPI 6: Product and Category Performance

**Definition:** Item sales value and item volume grouped by product or product category.

**Calculation:** Aggregate item prices and item counts by product or translated category.

**Business value:** Helps identify products and categories that contribute most to sales.

### KPI 7: Sales by Customer State

**Definition:** Item sales value grouped by customer state.

**Calculation:** Join orders to customers using `customer_id`, then aggregate item sales by state. Avoid double-counting when joining tables.

**Business value:** Helps identify geographic patterns in customer purchasing activity.

## 5. General Calculation Rules

1. Verify source files, column names, and join keys.
2. Count distinct `order_id` values for order-based metrics.
3. Aggregate order items appropriately before joining to other tables.
4. Define the order-status filters before calculating final KPIs.
5. Handle missing values and invalid records consistently.
6. Document the reporting period and exclusions.
7. Validate calculated totals against the underlying data.

## 6. Planned Visualizations

- Monthly sales trend.
- Monthly order volume.
- Top products or categories by item sales value.
- Sales by customer state.
- KPI summary cards for total orders, total item sales value, and average order value.

## 7. Pending Tasks

- [ ] Verify the required source CSV files and columns.
- [ ] Confirm order-status filters.
- [ ] Calculate and validate KPI values.
- [ ] Create the planned charts.
- [ ] Document findings and limitations.

## 8. Conclusion

These definitions provide a consistent starting point for sales analysis. The team will update this document if the actual data requires changes to the calculation methods.

**Status:** KPI definitions drafted; actual results pending validation.
