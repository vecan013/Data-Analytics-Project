# Delivery Performance and Customer Satisfaction Analysis
**Review Data Matching and Exclusions**

Out of 96,470 eligible delivered orders, 95,824 orders had matching customer review records and were included in the customer satisfaction analysis. The remaining 646 orders had no matching review records and were excluded from the review-score comparison.

All 95,824 matched orders had valid review scores. Therefore, the satisfaction analysis is based on 95,824 orders, while delivery performance calculations use 96,470 eligible delivered orders.
## 1. Objective

Analyze delivery performance and examine the relationship between delivery status and customer satisfaction using the Olist orders and order reviews datasets.

## 2. Dataset

- `olist_orders_dataset.csv`
- `olist_order_reviews_dataset.csv`

The datasets were loaded using Python and pandas. Date columns were converted to datetime format before calculating delivery durations.

## 3. Methodology

1. Inspected missing values and duplicate identifiers.
2. Selected delivered orders for delivery-time analysis.
3. Calculated delivery duration using purchase and actual delivery timestamps.
4. Compared actual delivery dates with estimated delivery dates to classify eligible orders as on-time or late.
5. Matched delivery records with review scores using `order_id`.
6. Generated summary CSV files and visualizations using pandas, Matplotlib, and Seaborn.

## 4. Delivery Performance Results

- Total delivered orders: 96,478
- Valid delivery-duration records: 96,470
- Average delivery time: 12.56 days
- Median delivery time: 10.22 days
- Eligible orders for on-time/late classification: 96,470
- On-time orders: 88,644 (91.89%)
- Late orders: 7,826 (8.11%)

Eight delivered orders were excluded from delivery-duration calculations because their dates were missing or invalid.

## 5. Customer Satisfaction Results

A total of 95,824 delivered orders were matched with review records for the comparison.

| Delivery status | Orders | Average review score | Median score |
|---|---:|---:|---:|
| On-time | 88,163 | 4.29 | 5 |
| Late | 7,661 | 2.57 | 2 |

Late deliveries were associated with lower average review scores than on-time deliveries. The difference in average scores was 1.72 points on a five-point scale.

These results show an association and do not establish that delivery delays alone caused lower customer ratings.

## 6. Visualizations

The following charts were generated:

- `output/charts/delivery_performance.png`
- `output/charts/customer_satisfaction.png`
- `output/charts/delivery_time_distribution.png`

## 7. Data Quality Considerations

- The orders dataset contains missing delivery timestamps for some orders.
- The review dataset contains missing review titles and comments.
- Duplicate review identifiers and repeated order IDs were detected.
- Review scores were averaged by order ID before merging to prevent multiple reviews from counting an order more than once in the satisfaction comparison.
- The maximum observed delivery duration was 209.63 days and should be investigated as a potential outlier.

## 8. Recommendations

1. Investigate the causes of late deliveries and prioritize reducing delays.
2. Review orders with unusually long delivery durations to identify data errors or operational issues.
3. Monitor review scores separately for late and on-time deliveries.
4. Improve delivery estimates and proactively communicate delays to customers.
5. Continue monitoring delivery performance and customer satisfaction over time.

## 9. Output Files

- `output/delivery_summary.csv`
- `output/customer_satisfaction_summary.csv`
- `output/charts/delivery_performance.png`
- `output/charts/customer_satisfaction.png`
- `output/charts/delivery_time_distribution.png`

## 10. Conclusion

The analysis found that 91.89% of eligible delivered orders arrived on time, while 8.11% arrived late. On-time deliveries had an average review score of 4.29, compared with 2.57 for late deliveries. Improving delivery reliability is therefore a reasonable priority for further investigation.

The results are based on the selected Olist datasets and should be interpreted with the data-quality limitations described above.