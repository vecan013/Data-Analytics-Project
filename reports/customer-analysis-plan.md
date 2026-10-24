# Customer Purchasing Behaviour Analysis Plan

**Prepared by:** C. R. Adharsh  
**Project:** Olist E-commerce Customer Analysis

## 1. Objective

The objective of this analysis is to understand customer purchasing behaviour using the Olist e-commerce dataset. The analysis focuses on customer identity, repeat purchasing, geographic distribution, monthly order trends, and RFM (Recency, Frequency, Monetary) segmentation.

Rather than reproducing large sections of raw CSV output, this document summarizes the main findings and explains what they indicate about customer behaviour.

## 2. Dataset Overview

The analysis uses three related datasets:

| Dataset | Purpose |
|---|---|
| `olist_customers_dataset.csv` | Contains customer identifiers and location details, including city, state, and ZIP-code prefix. |
| `olist_orders_dataset.csv` | Connects orders to customer records and contains order purchase timestamps and order statuses. |
| `olist_order_items_dataset.csv` | Contains order-item details, including item prices and freight charges. |

The tables are connected through `customer_id` and `order_id`. Item-level values are aggregated to the order level before customer-level spending is calculated, helping avoid counting an order multiple times.

### `customer_id` vs. `customer_unique_id`

- **`customer_id`** identifies a customer record associated with an order.
- **`customer_unique_id`** represents the underlying customer across potentially multiple customer records.

For repeat-purchase and RFM analysis, `customer_unique_id` is used to group purchases belonging to the same underlying customer.

## 3. Repeat-Customer Analysis

For this analysis, only orders with a `delivered` status are treated as eligible purchases.

- **One-time customer:** has exactly one eligible order.
- **Repeat customer:** has two or more distinct eligible orders.

The repeat-customer rate is calculated as:

\[
\text{Repeat-customer rate} =
\frac{\text{Number of repeat customers}}
{\text{Total eligible unique customers}} \times 100
\]

### Key findings

The saved analysis reports **93,358 unique customers** with eligible delivered purchases. Of these:

- **90,557 customers (approximately 97.00%)** made one eligible purchase.
- **2,801 customers (approximately 3.00%)** made two or more eligible purchases.

### Interpretation

The customer base is dominated by one-time purchasers. This suggests that encouraging a second purchase could be an important retention opportunity. Follow-up campaigns, relevant product recommendations, and post-purchase engagement could be tested to encourage customers to return. These are potential actions to investigate, not proof that any particular campaign will improve retention.

## 4. Customer Location Analysis

Customer geography is analyzed using `customer_state`, `customer_city`, and `customer_zip_code_prefix`. State-level and city-level summaries compare customer counts, order counts, and item revenue. Freight charges are summarized separately from item revenue.

### Customer distribution by state

The highest customer counts are concentrated in the following states:

| State | Unique customers | Orders | Item revenue |
|---|---:|---:|---:|
| São Paulo (SP) | 39,156 | 40,501 | 5,067,633.16 |
| Rio de Janeiro (RJ) | 11,917 | 12,350 | 1,759,651.13 |
| Minas Gerais (MG) | 11,001 | 11,354 | 1,552,481.83 |
| Rio Grande do Sul (RS) | 5,168 | 5,345 | 728,897.47 |
| Paraná (PR) | 4,769 | 4,923 | 666,063.51 |

São Paulo is the largest market in the saved state-level results, leading the other states in both customer count and item revenue. Rio de Janeiro and Minas Gerais follow.

### Customer distribution by city

The leading cities by unique customer count are:

| State | City | Unique customers | Orders | Item revenue |
|---|---|---:|---:|---:|
| SP | São Paulo | 14,528 | 15,045 | 1,859,556.83 |
| RJ | Rio de Janeiro | 6,361 | 6,601 | 955,573.97 |
| MG | Belo Horizonte | 2,606 | 2,697 | 346,039.04 |
| DF | Brasília | 2,013 | 2,071 | 295,814.72 |
| PR | Curitiba | 1,434 | 1,489 | 205,999.33 |

São Paulo city has the highest customer count and item revenue among the listed cities. The city-level results also show that customer demand is concentrated in a relatively small set of major urban areas, while the wider dataset contains customers from many other cities.

### Interpretation

- São Paulo is the strongest geographic market in the saved results.
- Rio de Janeiro and Minas Gerais are also important markets based on customer volume and item revenue.
- City-level summaries can help prioritize regional marketing, customer support, and delivery-performance investigations.
- Customer counts and revenue are descriptive measures; they do not by themselves explain why customers are concentrated in particular locations.

## 5. Purchasing-Pattern Analysis

Monthly purchasing trends are summarized using the number of distinct delivered orders, item revenue, and freight totals.

### Key findings

- The saved monthly output covers **23 purchase-month entries**, from September 2016 to August 2018.
- November 2017 has the highest order count in the monthly summary, with **7,289 orders**.
- November 2017 also has the highest monthly item revenue in the saved results, at approximately **987,765.37**.
- Monthly order volume rises substantially through 2017, with high activity continuing into the first half of 2018.

### Interpretation

The monthly results indicate an overall increase in order activity during the period covered, with a notable peak in November 2017. This peak may warrant further investigation alongside promotions, seasonal shopping events, and marketing activity. The dataset alone does not establish which factor caused the increase.

## 6. RFM Customer Segmentation

RFM stands for **Recency, Frequency, and Monetary value**. It provides a rule-based way to group customers according to how recently they purchased, how often they purchased, and how much they spent.

### Metrics

- **Recency (R):** Number of days between the analysis snapshot date and a customer's most recent eligible purchase. Fewer days means a more recent purchase.
- **Frequency (F):** Number of distinct eligible orders placed by the customer.
- **Monetary (M):** Sum of item prices across the customer's eligible orders. Freight is excluded from this RFM monetary value.

The snapshot date is set to the day after the latest eligible purchase date. Only delivered orders are included in the current analysis.

### Scoring rules

Each metric receives a score from **1 to 5**:

| Metric | Score of 1 | Score of 5 |
|---|---|---|
| Recency | Less recent purchase | Most recent purchase |
| Frequency | Lower order frequency | Higher order frequency |
| Monetary | Lower item spending | Higher item spending |

The tie-aware scoring method uses percentile ranks (`rank(method="average", pct=True)`) so customers with identical metric values receive the same percentile rank before the percentile is converted to a score. This avoids assigning different Frequency scores to customers who have the same purchase count simply because they appear in a different row order.

The three scores are concatenated to form an `RFM_score`. For example, `454` means R = 4, F = 5, and M = 4.

### Segment rules

| Segment | Rule |
|---|---|
| **Champions** | R ≥ 4, F ≥ 4, and M ≥ 4 |
| **Loyal** | F ≥ 4 and R ≥ 3 |
| **Potential Loyalists** | R ≥ 4 and F ≤ 2 |
| **At Risk** | R ≤ 2 and F ≥ 3 |
| **Hibernating** | R ≤ 2 and F ≤ 2 |
| **Needs Attention** | All other combinations |

The rules are applied in the order shown in the Python code. Monetary score is explicitly part of the Champions condition; the other listed segment rules use Recency and Frequency.

### Summary of the saved RFM results

| Segment | Customers | Total monetary value | Mean frequency | Mean recency (days) |
|---|---:|---:|---:|---:|
| Needs Attention | 54,165 | 7,412,973.88 | 1.000 | 134.02 |
| At Risk | 37,389 | 5,328,881.99 | 1.029 | 394.96 |
| Champions | 931 | 305,122.29 | 2.189 | 89.27 |
| Loyal | 873 | 174,519.95 | 2.071 | 177.23 |

These saved results list four segments. No customers appear under Potential Loyalists or Hibernating in this particular summary.

### Interpretation

- **Needs Attention** is the largest segment, and its mean frequency of 1.0 indicates that customers in this group generally made one eligible purchase.
- **At Risk** customers have a high mean recency of approximately 395 days, indicating that their latest purchase was much further in the past than that of other listed segments.
- **Champions** have the highest mean frequency among the listed segments and a relatively low mean recency, consistent with more recent and repeated purchasing.
- **Loyal** customers also have a mean frequency above two purchases, although their average recency is higher than that of Champions.

These segments can support targeted retention strategies. For example, the business could investigate win-back approaches for At Risk customers and repeat-purchase incentives for customers who have purchased only once. These recommendations should be evaluated using subsequent campaign and purchasing data.

**Results note:** The segment counts above describe the saved output provided for this analysis. Rerunning the script with the corrected tie-aware RFM scoring may change the segment distribution, so the summary should be refreshed after the latest run.

## 7. Main Conclusions

1. **Repeat purchasing is limited:** approximately 3% of eligible unique customers are classified as repeat customers in the saved results.
2. **Demand is geographically concentrated:** São Paulo leads the state and city summaries by customer count and item revenue.
3. **Order activity changes over time:** monthly order volume grows during the period covered, with a peak in November 2017.
4. **RFM supports differentiated customer treatment:** the saved summary contains large Needs Attention and At Risk groups, alongside smaller Champions and Loyal groups.
5. **Customer retention is a useful area for further investigation:** follow-up analysis could test ways to increase second purchases and re-engage inactive customers.

## 8. Output Files

The Python analysis writes detailed tables and charts to the configured output directory.

| Output file | Purpose |
|---|---|
| `order_level_analysis.csv` | Order-level data with item value, freight, item count, and total including freight. |
| `customer_order_frequency.csv` | Customer-level order count, spend, first and last purchase, and one-time/repeat classification. |
| `repeat_customer_summary.csv` | Overall one-time and repeat-customer counts and repeat rate. |
| `repeat_customers.png` | Bar chart comparing one-time and repeat customers. |
| `location_by_state.csv` | Customer count, order count, item revenue, and freight by state. |
| `location_by_city.csv` | Customer count, order count, and item revenue by city and state. |
| `repeat_rate_by_state.csv` | Repeat-customer counts and repeat rate by state. |
| `customers_by_state.png` | Chart of the top 10 states by unique customer count. |
| `order_value_descriptive_stats.csv` | Descriptive statistics for item value, freight, and total order value including freight. |
| `monthly_purchasing_trends.csv` | Monthly order counts, item revenue, and freight totals. |
| `orders_by_month.png` | Line chart of eligible orders by month. |
| `rfm_customer_segments.csv` | Customer-level RFM metrics, scores, segment, and snapshot date. |
| `rfm_segment_summary.csv` | Customer counts and summary metrics for each RFM segment. |

## 9. Scope and Limitations

- The current analysis treats only `delivered` orders as eligible purchases.
- RFM monetary value is based on item prices and excludes freight.
- Segment labels are rule-based summaries of historical behaviour, not predictions of future customer behaviour.
- The monthly patterns show association over time; they do not establish the cause of a peak or decline.
- The saved RFM segment summary should be regenerated after any change to the scoring logic so the written findings match the latest outputs.
