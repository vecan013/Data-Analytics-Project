# Sales Analysis Findings

## 1. Objective

Analyze Olist e-commerce sales data to identify monthly sales trends and the product categories generating the highest item sales value.

## 2. Key Metrics

- **Delivered orders:** 96,478
- **Total item sales value:** R$ 13,221,498.11
- **Average item sales value per delivered order:** R$ 137.04

*Note: Monetary values are expressed in Brazilian reais (R$). Item sales value is calculated using product item prices and excludes freight charges. These figures represent sales value, not profit.*

## 3. Top Product Categories
The top categories by item sales value are:

1. Health & Beauty — 1,233,131.72
2. Watches & Gifts — 1,166,176.98
3. Bed, Bath & Table — 1,023,434.76
4. Sports & Leisure — 954,852.55
5. Computers & Accessories — 888,724.61
6. Furniture & Decor — 711,927.69
7. Housewares — 615,628.69
8. Cool Stuff — 610,204.10
9. Auto — 578,966.65
10. Toys — 471,286.48

## 4. Visualizations
- Monthly item sales trend: `output/monthly_sales.png`
- Top 10 product categories: `output/top_product_categories.png`

## 5. Initial Business Insights
- Health & Beauty generated the highest item sales value among the analyzed categories.
- Watches & Gifts ranked second.
- Bed, Bath & Table ranked third.
- These categories may deserve further investigation for product-level performance and marketing opportunities.
- Monthly trends should be reviewed to identify periods of higher or lower item sales value.

## 6. Limitations
- The analysis uses item prices and excludes freight charges.
- The findings describe item sales value, not profit, because product costs and operating expenses are not included.
- Monthly patterns should be interpreted using the generated chart and underlying CSV.
- These results are preliminary and should be validated before making business decisions.

## 7. Files Generated
- `output/monthly_sales.csv`
- `output/top_product_categories.csv`
- `output/monthly_sales.png`
- `output/top_product_categories.png`

## 8. Monthly Sales Analysis

Monthly sales were analyzed using SQL and Python, grouping delivered orders by their purchase timestamps.

- The dataset covers the period from 2016 to 2018.
- November 2017 recorded 7,289 delivered orders and R$ 987,765.37 in item sales value in the verified SQL results.
- Monthly sales values vary across the observed period.

**Interpretation note:** A chart grouped only by month name combines the same month across different years. Use the Year slicer or a Year-Month field to examine chronological trends.

## 9. Payment Method Analysis


| Payment Method | Payment Records | Total Payment Value | Average per Record |
|---|---:|---:|---:|
| Credit card | 76,795 | R$ 12,542,084.19 | R$ 163.32 |
| Boleto | 19,784 | R$ 2,869,361.27 | R$ 145.03 |
| Voucher | 5,775 | R$ 379,436.87 | R$ 65.70 |
| Debit card | 1,529 | R$ 217,989.79 | R$ 142.57 |
| Not defined | 3 | R$ 0.00 | R$ 0.00 |

### Findings

- Credit cards recorded the highest total payment value.
- Boleto was the second-largest payment method by total payment value.
- Voucher payments had the lowest average payment value among the major payment methods.

**Note:** These are payment-record counts, not distinct order counts. Payment values are not directly equivalent to item sales value.

## 10. Delivery Performance

Delivery performance was measured by comparing actual customer delivery dates with estimated delivery dates.

| Metric | Result |
|---|---:|
| Delivered orders with both dates available | 96,470 |
| Late-delivered orders | 7,826 |
| Late-delivery percentage | 8.11% |

### Findings

- A total of 7,826 orders were delivered later than their estimated dates.
- The late-delivery rate was 8.11% among delivered orders with both dates available.

### Business implications

Investigate late deliveries by seller, destination, and time period to identify possible logistics issues. Additional review-score analysis is needed before drawing conclusions about the impact of delays on customer satisfaction.

## 11. Business Recommendations

1. **Focus on leading categories:** Investigate products and marketing strategies contributing to sales in health and beauty, watches and gifts, and bed, bath and table.
2. **Monitor sales trends:** Compare monthly sales by year to distinguish seasonal patterns from changes over time.
3. **Track payment methods:** Monitor payment values and counts while accounting for orders with multiple payment records.
4. **Investigate delivery delays:** Examine late deliveries to identify recurring operational problems.
5. **Improve dashboard usability:** Retain the KPI cards, Year slicer, monthly sales chart, and top-category chart.
6. **Extend customer analysis:** Analyze repeat purchases, customer segments, and review scores to gain additional insight into customer behavior.

These recommendations identify areas for further investigation; the current results do not establish causation or profitability.

## 12. Conclusion

The analysis identified R$ 13,221,498.11 in item sales value across 96,478 delivered orders, with an average item sales value of R$ 137.04 per delivered order. Health and beauty ranked first among the analyzed product categories, and credit cards accounted for the largest payment value. The delivery analysis found that 8.11% of eligible delivered orders arrived late.

The Python, SQL, and Power BI work provides a foundation for monitoring sales performance and investigating operational improvements. Further customer purchasing behavior and satisfaction analysis can extend the overall Olist E-Commerce Analytics project.
