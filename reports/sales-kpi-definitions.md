# Sales KPI Definitions — Olist E-commerce Analytics

## 1. Purpose

This document defines the key performance indicators (KPIs) for analyzing sales performance in the Olist Brazilian E-Commerce dataset.

These metrics will help the Zaalima team understand order trends, sales value, customer purchasing behavior, and product performance.

**Status:** Initial draft. KPI values will be calculated and validated during analysis.

## 2. Data Sources

The following datasets are expected to support the sales analysis:

- `olist_orders_dataset.csv`
- `olist_order_items_dataset.csv`
- `olist_order_payments_dataset.csv`
- `olist_products_dataset.csv`
- `product_category_name_translation.csv`

The availability of these files and the required columns must be verified before calculating the KPIs.

## 3. Key Performance Indicators

### KPI 1: Total Orders

**Definition:** The number of distinct orders included in the analysis.

**Calculation:** Count distinct `order_id` values.

**Business purpose:** Measures order volume and helps identify changes in purchasing activity.

**Important:** Define which order statuses are included before comparing results.

### KPI 2: Total Sales Value

**Definition:** The total value of order items included in the analysis.

**Calculation:** Sum the `price` column in `olist_order_items_dataset.csv` for the selected orders.

**Business purpose:** Helps measure sales performance and compare trends across time periods.

**Important:** This metric represents item value, not necessarily total customer payment. Freight charges, payment adjustments, cancellations, and refunds must be handled consistently.

### KPI 3: Average Order Value (AOV)

**Definition:** The average item sales value per distinct order.

**Calculation:**

Average Order Value = Total Item Sales Value / Number of Distinct Included Orders

**Business purpose:** Helps understand the average value of an order and whether customers are placing higher-value or lower-value orders.

**Important:** Use the same order population in the numerator and denominator.

### KPI 4: Monthly Sales Trend

**Definition:** The change in item sales value across calendar months.

**Calculation:** Group included order-item sales by month using the appropriate order date, then sum `price`.

**Business purpose:** Identifies seasonal patterns, growth, and declines in sales.

**Important:** Document the chosen order date and treatment of cancelled or unavailable orders.

### KPI 5: Monthly Order Trend

**Definition:** The number of distinct orders placed in each calendar month.

**Calculation:** Group orders by purchase month and count distinct `order_id`.

**Business purpose:** Shows how order volume changes over time.

### KPI 6: Product and Category Performance

**Definition:** The sales value and order-item volume associated with each product or product category.

**Calculation:** Aggregate item `price` and item counts by product or translated product category.

**Business purpose:** Identifies products and categories that contribute most to sales.

**Important:** Join product information using `product_id` and verify the category translation mapping where available.

### KPI 7: Sales by Customer State

**Definition:** The item sales value associated with customers in each state.

**Calculation:** Aggregate included order-item sales by customer state after joining orders to customer records.

**Business purpose:** Helps identify geographic differences in purchasing activity.

**Important:** Avoid double-counting sales when joining datasets that contain multiple rows per order.

## 4. General Calculation Rules

1. Verify the relevant columns and relationships before analysis.
2. Count distinct `order_id` values when measuring orders.
3. Aggregate order items before joining to other tables where necessary to prevent duplicate sales totals.
4. Define included order statuses and apply the same rules consistently.
5. Handle missing dates, missing customer locations, and invalid numeric values transparently.
6. Record the date range and filters used in each report.
7. Validate totals against the underlying source data.

## 5. Planned Visualizations

- Monthly sales trend line chart.
- Monthly order volume chart.
- Top products or categories by item sales value.
- Sales value by customer state.
- KPI summary cards for total orders, total item sales value, and average order value.

## 6. Expected Deliverables

- A documented KPI definition for each metric.
- Reproducible calculations using Python or SQL.
- Charts and summary tables showing sales performance.
- A findings report explaining important trends and limitations.

## 7. Pending Tasks

- [ ] Verify source CSV files and required columns.
- [ ] Finalize the order-status inclusion rule.
- [ ] Calculate and validate all KPI values.
- [ ] Generate visualizations.
- [ ] Document findings and limitations.

## 8. Conclusion

These KPI definitions establish a consistent starting point for sales analysis in the Olist E-commerce project. The definitions and calculations should be reviewed against the available data before final results are reported.
