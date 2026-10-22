# Delivery Performance & Customer Satisfaction Analysis Plan

## 1. Objective
The objective of this analysis is to evaluate delivery performance and customer satisfaction in the Olist e-commerce platform. We will examine delivery times, identify late deliveries, analyze customer review scores, and investigate the relationship between delivery performance and customer satisfaction.

## 2. Business Questions
1. What is the average delivery time for orders?
2. How many orders were delivered on time and how many were late?
3. What percentage of eligible orders were delivered on time?
4. What is the average customer review score?
5. Which review scores occur most frequently?
6. Do late deliveries tend to receive lower review scores?
7. How does delivery performance change from month to month?

## 3. Dataset Tables
The following CSV files will be used:
- `olist_orders_dataset.csv` — order status, purchase timestamps, estimated delivery dates, and actual delivery dates.
- `olist_order_reviews_dataset.csv` — customer review scores and review information.
- `olist_order_items_dataset.csv` — products and order-item details, if required for additional analysis.

## 4. Key Metrics
| Metric | Definition |
|---|---|
| Average Delivery Time | Average number of days between purchase and delivery |
| On-Time Orders | Orders delivered on or before the estimated delivery date |
| Late Orders | Orders delivered after the estimated delivery date |
| On-Time Delivery Rate | On-time delivered orders divided by eligible delivered orders, multiplied by 100 |
| Average Review Score | Average of available customer review scores |
| Review Score by Delivery Status | Average review score for on-time and late deliveries |
| Monthly Delivery Performance | Delivery metrics grouped by month |

## 5. Analysis Methodology
1. Inspect the relevant CSV files and understand their columns.
2. Check for missing values, duplicate records, and inconsistent dates.
3. Convert date columns into the correct datetime format.
4. Calculate delivery time using purchase and actual delivery timestamps.
5. Compare actual delivery dates with estimated delivery dates.
6. Calculate the number and percentage of on-time and late deliveries.
7. Analyze the distribution of customer review scores.
8. Compare review scores for on-time and late deliveries.
9. Group delivery metrics by month to identify trends.
10. Summarize the findings and suggest possible business improvements.

## 6. Data Quality Considerations
- Exclude canceled orders from delivery-time calculations.
- Handle orders with missing delivery timestamps carefully.
- Use only eligible delivered orders when calculating delivery performance.
- Check for multiple review records before joining orders with reviews.
- Avoid double-counting orders when joining tables.
- Define the eligible order population clearly for each metric.
- Treat any relationship between delivery delays and review scores as an association, not proof of causation.

## 7. Suggested Visualizations
- Bar chart: On-time vs. late orders.
- KPI cards: Average delivery time, on-time delivery rate, and average review score.
- Bar chart: Distribution of customer review scores.
- Bar chart: Average review score by delivery status.
- Line chart: Monthly delivery performance.

## 8. Expected Deliverables
- A documented delivery performance analysis plan.
- Definitions of delivery and customer satisfaction metrics.
- A plan for comparing delivery status with customer review scores.
- Suggested visualizations.
- A summary of actual findings after the data analysis is completed.

## 9. Status
Current status: Analysis planning.

Next step: Inspect the relevant CSV files and begin the analysis after the plan is reviewed.