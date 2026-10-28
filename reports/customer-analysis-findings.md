# Customer Purchasing Behavior Analysis — Findings

## 1. Objective

Analyze customer purchasing behavior in the Olist e-commerce dataset, focusing on repeat purchasing, customer geography, monthly delivered-order trends, product-category sales, average order value (AOV), and RFM segmentation.

## 2. Data and Methodology

The analysis used five local CSV datasets: customers, orders, order items, products, and product-category translations.

For customer and trend analysis, eligible orders were defined as orders with `order_status == "delivered"` and a valid purchase timestamp. Duplicate order IDs were removed before customer-level analysis. `customer_unique_id` was used to identify underlying customers, and distinct order IDs were used to calculate purchase frequency.

Product-category sales were calculated by summing item prices, excluding freight. AOV was calculated from product prices plus freight, with each eligible order counted once. RFM scores were calculated using quintiles, with recency scored in reverse so that more recent purchases received higher scores.

## 3. Key Customer Metrics

| Metric | Result |
|---|---:|
| Eligible delivered orders | 96,478 |
| Unique customers | 93,358 |
| One-time customers | 90,557 |
| Repeat customers | 2,801 |
| Repeat customer rate | 3.00% |
| Average orders per customer | 1.033 |

Most eligible customers placed only one delivered order. The repeat-customer rate was approximately 3%, suggesting a potential retention opportunity. The data describes purchasing behavior within the available observation period and does not establish why customers did not return.

## 4. Customer Location Analysis

The states with the largest eligible unique-customer populations were:

| State | Unique customers |
|---|---:|
| SP | 39,156 |
| RJ | 11,917 |
| MG | 11,001 |
| RS | 5,168 |
| PR | 4,769 |
| SC | 3,449 |
| BA | 3,158 |
| DF | 2,019 |
| ES | 1,928 |
| GO | 1,895 |

SP had the largest customer population, followed by RJ and MG. The customer base is geographically concentrated in these states. Customer counts alone do not establish which states have the highest spending, profitability, or growth potential.

The top-state visualization is saved as `output/top_customer_states.png`.

## 5. Monthly Delivered-Order Trends

Monthly delivered orders were grouped by purchase month. The chart shows substantial growth from late 2016 through 2017, reaching a peak of approximately 7,300 orders in November 2017. Monthly counts remained comparatively high into 2018, followed by lower counts during parts of the middle of that year.

These counts include orders that were ultimately delivered, grouped by their purchase dates. The trend does not establish the cause of monthly peaks or declines. Partial months and the boundaries of the dataset should be considered when comparing periods.

The visualization is saved as `output/monthly_order_trends.png`.

## 6. Product Category Analysis

The top categories by product sales value, excluding freight, were:

| Category | Product sales (BRL) | Items sold |
|---|---:|---:|
| Health & beauty | 1,233,131.72 | 9,465 |
| Watches & gifts | 1,166,176.98 | 5,859 |
| Bed, bath & table | 1,023,434.76 | 10,953 |
| Sports & leisure | 954,852.55 | 8,431 |
| Computers & accessories | 888,724.61 | 7,644 |
| Furniture & decor | 711,927.69 | 8,160 |
| Housewares | 615,628.69 | 6,795 |
| Cool stuff | 610,204.10 | 3,718 |
| Auto | 578,966.65 | 4,140 |
| Toys | 471,286.48 | 4,030 |

Health & beauty had the highest product sales value among the categories analyzed. Bed, bath & table sold more items than health & beauty but generated less sales value, illustrating that item volume and sales value measure different aspects of performance.

These figures represent sales value, not profit, because product costs and operating expenses were not included.

The visualization is saved as `output/top_product_categories.png`.

## 7. Average Order Value

| Metric | Value (BRL) |
|---|---:|
| Total product value | 13,221,498.11 |
| Total freight value | 2,198,275.64 |
| Total order value | 15,419,773.75 |
| Eligible delivered orders | 96,478 |
| Average order value | 159.83 |

AOV was R$159.83, calculated by dividing the total value of product prices plus freight by the number of eligible delivered orders. Each order was counted once in the denominator, even when it contained multiple items.

## 8. RFM Customer Segmentation

RFM scores were calculated using quintiles. Recency was scored in reverse, while frequency and monetary scores increased with higher values. The reference date was one day after the latest eligible purchase date.

| Segment | Customers | Average monetary value (BRL) | Average frequency |
|---|---:|---:|---:|
| Other Customers | 37,953 | 150.19 | 1.00 |
| Needs Re-engagement | 31,352 | 137.20 | 1.01 |
| Recent and Frequent | 14,908 | 176.92 | 1.09 |
| Frequent High Spenders | 9,145 | 304.03 | 1.15 |

The largest segment was Other Customers. Needs Re-engagement represented 31,352 customers, while Frequent High Spenders had the highest average monetary value at R$304.03.

These are simplified, rule-based segments rather than validated loyalty classifications. Average purchase frequencies close to one indicate that even customers assigned to the higher-frequency segments generally had few delivered orders. Quintile scoring with rank-based tie handling can also assign different scores to customers with tied underlying values.

The visualization is saved as `output/rfm_customer_segments.png`.

## 9. Business Recommendations

1. **Test customer-retention campaigns.** Investigate whether targeted follow-ups, relevant product recommendations, or post-purchase offers improve the repeat-purchase rate. Evaluate results using a defined measurement period.
2. **Prioritize geographic analysis.** Use SP, RJ, and MG as starting points for examining sales value, delivery performance, and customer acquisition opportunities. Customer volume alone should not determine investment.
3. **Review high-value product categories.** Investigate inventory availability, pricing, and customer demand in health & beauty, watches & gifts, and bed, bath & table. Sales value should be considered alongside item volume and, where available, profitability.
4. **Use AOV as a monitoring metric.** Track AOV over time and across categories or states to identify differences in order value. Any promotion intended to increase AOV should also be evaluated for its effect on profit.
5. **Validate RFM segments before deployment.** Test whether the proposed segments predict future repeat purchases or revenue. Refine the thresholds and account for the dataset's historical observation period before using them for live customer targeting.

## 10. Limitations

- The analysis covers the records available in the supplied dataset and uses delivered orders with valid purchase timestamps for the principal customer metrics.
- Missing delivery and approval timestamps occur in the original orders data; orders were not included in the eligible population unless their status was delivered and their purchase timestamp was valid.
- Some product records have missing category names. Unknown categories were retained rather than silently discarded.
- Customer counts do not measure profitability or explain customer motivations.
- The RFM reference date is historical and based on the latest eligible purchase, so the scores do not describe current activity.
- Rank-based quintile scoring can split tied values across score groups. The simplified segment labels should be validated before business deployment.
- Monthly counts may be affected by partial periods and dataset boundaries.
