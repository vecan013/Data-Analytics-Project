# Customer Analysis Findings

**Project:** Olist E-commerce Customer Analysis

## Objective

This report documents the customer and order data used, explains the
customer identifiers, defines repeat purchasing, summarizes customer
geography and purchasing patterns, and outlines an RFM segmentation
approach supported by the available data.

## 1. Identify the customer and order tables

The analysis uses these Olist datasets:

  -----------------------------------------------------------------------
  Dataset                             Role
  ----------------------------------- -----------------------------------
  `olist_customers_dataset.csv`       Customer record identifiers and
                                      location fields, including city,
                                      state, and ZIP-code prefix.

  `olist_orders_dataset.csv`          Links orders to customer records
                                      and provides order timestamps and
                                      order statuses.

  `olist_order_items_dataset.csv`     Provides item-level prices and
                                      freight charges for each order.
  -----------------------------------------------------------------------

The tables are joined using `customer_id` and `order_id`. Item values
are aggregated to one row per order before customer spending is
calculated, preventing order totals from being counted repeatedly across
item rows.

For a conservative completed-purchase analysis, only orders with
`order_status = delivered` are included. The supplied order-level output
contains **99,441 orders**: **96,478 delivered** and **2,963 with other
statuses**. Non-delivered orders are excluded from the relevant
repeat-purchase, location, purchasing-pattern, and RFM calculations.
Orders missing a valid customer identifier or purchase timestamp are
also excluded from RFM where required.

## 2. Explain `customer_id` versus `customer_unique_id`

-   **`customer_id`** identifies a customer record associated with an
    order.
-   **`customer_unique_id`** identifies the underlying customer across
    potentially multiple customer records.

For customer-level repeat-purchase analysis and RFM segmentation,
`customer_unique_id` is used so that purchases associated with the same
underlying customer can be grouped together.

## 3. Define how repeat customers are identified

A repeat customer is a customer with **two or more distinct eligible
delivered orders**. A one-time customer has exactly one distinct
eligible delivered order. The repeat-customer rate is calculated as:

**Repeat-customer rate** = (repeat customers ÷ all eligible unique
customers) × 100

### Results

  Measure                       Result
  --------------------------- --------
  Eligible unique customers     93,358
  One-time customers            90,557
  Repeat customers               2,801
  Repeat-customer rate           3.00%
  Eligible delivered orders     96,478

Most eligible customers made only one delivered purchase. Encouraging a
second purchase and testing relevant post-purchase engagement are
potential retention opportunities; their impact would need to be
measured.

## 4. Propose customer location and purchasing-pattern analyses

### Customer location

Customer location summaries use state and city, ranked by unique
customer count. The complete results are available in
`location_by_state.csv` and `location_by_city.csv`.

**Top five states by unique customer count**

  State     Unique customers   Orders   Item revenue   Freight total
  ------- ------------------ -------- -------------- ---------------
  SP                  39,156   40,501   5,067,633.16      702,069.99
  RJ                  11,917   12,350   1,759,651.13      295,750.44
  MG                  11,001   11,354   1,552,481.83      266,409.84
  RS                   5,168    5,345     728,897.47      132,575.32
  PR                   4,769    4,923     666,063.51      115,645.29

São Paulo (SP) is the largest state market in the saved results,
followed by Rio de Janeiro (RJ) and Minas Gerais (MG).

**Top five cities by unique customer count**

  City (state)            Unique customers   Orders   Item revenue
  --------------------- ------------------ -------- --------------
  Sao Paulo (SP)                    14,528   15,045   1,859,556.83
  Rio De Janeiro (RJ)                6,361    6,601     955,573.97
  Belo Horizonte (MG)                2,606    2,697     346,039.04
  Brasilia (DF)                      2,013    2,071     295,814.72
  Curitiba (PR)                      1,434    1,489     205,999.33

São Paulo city leads the saved city-level results, followed by Rio de
Janeiro and Belo Horizonte. Customer counts, order counts, item revenue,
freight totals, and repeat-customer rates can be compared by geography
to help prioritize regional analysis. Customer counts alone do not
explain why the distribution occurs.

### Purchasing patterns

The script summarizes eligible delivered orders by purchase month,
including distinct order count, item revenue, and freight totals. The
saved output covers **23 purchase-month entries from September 2016 to
August 2018**.

-   **November 2017** was the highest month in the saved monthly output,
    with **7,289 delivered orders** and item revenue of **987,765.37**.
-   Monthly order volume generally increased through 2017 and remained
    high during much of the first half of 2018.

Monthly trends can be examined alongside promotions or seasonal
activity, but the descriptive results alone do not establish the cause
of the November peak. Order-value descriptive statistics can also be
used to compare item value, freight, and total order value.

## 5. Outline an RFM segmentation approach

The available data supports RFM segmentation using eligible delivered
orders grouped by `customer_unique_id`.

### RFM metrics

-   **Recency (R):** Number of days between the snapshot date and the
    customer's latest eligible purchase. The snapshot date is the day
    after the latest eligible purchase date in the data. Fewer days
    means a more recent purchase.
-   **Frequency (F):** Number of distinct eligible `order_id` values for
    the customer.
-   **Monetary (M):** Sum of item value across the customer's eligible
    orders. Freight is excluded from RFM monetary value.

### Scoring

Each metric receives a score from 1 to 5:

  Metric      Higher score means
  ----------- ---------------------------------------------------
  Recency     More recent purchase (fewer days since purchase).
  Frequency   More distinct delivered orders.
  Monetary    Higher total item spending.

The implementation uses percentile ranks
(`rank(method="average", pct=True)`), multiplies by 5, rounds upward
using `ceil`, and clips scores to the 1--5 range. Recency is ranked in
descending order so lower recency values receive higher scores.
Frequency and Monetary are ranked in ascending order so higher values
receive higher scores. Tied values receive the same score, so score
groups do not necessarily contain exactly 20% of customers each.

The three scores are concatenated into `RFM_score`; for example, `454`
means R=4, F=5, M=4.

### Segment rules

The implementation applies these rules in order:

  -----------------------------------------------------------------------
  Segment                 Rule                    Interpretation
  ----------------------- ----------------------- -----------------------
  **Champions**           R ≥ 4, F ≥ 4, M ≥ 4     Recent, frequent,
                                                  high-spending
                                                  customers.

  **Loyal**               F ≥ 4 and R ≥ 3         Frequent customers
                                                  whose purchases are
                                                  reasonably recent.

  **Potential Loyalists** R ≥ 4 and F ≤ 2         Recent customers with
                                                  low purchase frequency.

  **At Risk**             R ≤ 2 and F ≥ 3         Less-recent customers
                                                  with moderate or high
                                                  frequency scores.

  **Hibernating**         R ≤ 2 and F ≤ 2         Less-recent customers
                                                  with low frequency
                                                  scores.

  **Needs Attention**     All other combinations  Customers not captured
                                                  by the rules above.
  -----------------------------------------------------------------------

### Saved RFM results

  ----------------------------------------------------------------------------
  Segment          Customers      Total monetary Mean frequency   Mean recency
                                           value                        (days)
  ----------- -------------- ------------------- -------------- --------------
  Needs               54,165        7,412,973.88          1.000         134.02
  Attention                                                     

  At Risk             37,389        5,328,881.99          1.029         394.96

  Champions              931          305,122.29          2.189          89.27

  Loyal                  873          174,519.95          2.071         177.23

  **Total**       **93,358**   **13,221,498.11**            ---            ---
  ----------------------------------------------------------------------------

The saved summary contains four populated segments; the rules for
Potential Loyalists and Hibernating are defined, but those segments do
not appear in this saved summary. The results suggest that many
customers have low purchase frequency, while the Champions and Loyal
groups are comparatively small. Segment-specific retention or
re-engagement actions can be tested and measured.

## Validation and limitations

The supplied derived outputs reconcile internally:

-   `rfm_customer_segments.csv` contains **93,358 unique customers**,
    matching the eligible unique-customer count in
    `repeat_customer_summary.csv`.
-   The four populated segment counts sum to **93,358**.
-   Recalculating customer counts and monetary totals from
    `rfm_customer_segments.csv` reproduces the saved
    `rfm_segment_summary.csv` values, with monetary totals matching to
    two decimal places.
-   Re-aggregating delivered rows in `order_level_analysis.csv` produces
    **93,358 customers**, **96,478 distinct orders**, and total item
    value of **13,221,498.11**. These match the RFM customer count,
    summed frequency, and total monetary value.

The supplied `output.zip` includes derived files such as
`order_level_analysis.csv`, `rfm_customer_segments.csv`, and
`rfm_segment_summary.csv`, but not the three original raw Olist input
CSVs. Therefore, internal reconciliation passed, but a fresh end-to-end
validation against the original source files cannot be claimed. Rerun
the script using the original inputs before treating the results as
fully source-validated. Refresh the saved segment counts after changes
to scoring or input data.

## Conclusion

The saved analysis indicates that most eligible customers made only one
delivered purchase, São Paulo is the largest geographic market, and
monthly order activity peaked in November 2017. RFM segmentation adds a
customer-level view of recency, repeat frequency, and item spending that
can help identify groups for retention or re-engagement experiments.
These are descriptive findings; further analysis is needed to explain
the observed patterns and evaluate the impact of any business actions.

## Output files

  -------------------------------------------------------------------------
  Output                                Purpose
  ------------------------------------- -----------------------------------
  `order_level_analysis.csv`            Order-level customer, status, item
                                        value, freight, and order totals.

  `customer_order_frequency.csv`        Customer order counts, spend,
                                        first/last purchase, and
                                        one-time/repeat label.

  `repeat_customer_summary.csv`         Overall eligible customer counts
                                        and repeat rate.

  `repeat_customers.png`                One-time versus repeat customer
                                        chart.

  `location_by_state.csv`               Full state-level location summary.

  `location_by_city.csv`                Full city-level location summary.

  `repeat_rate_by_state.csv`            Repeat-customer rate by state.

  `customers_by_state.png`              Top 10 states by unique customer
                                        count.

  `order_value_descriptive_stats.csv`   Descriptive statistics for item
                                        value, freight, and total order
                                        value.

  `monthly_purchasing_trends.csv`       Monthly order counts, item revenue,
                                        and freight totals.

  `orders_by_month.png`                 Monthly order-count chart.

  `rfm_customer_segments.csv`           Customer-level RFM metrics, scores,
                                        segment, and snapshot date.

  `rfm_segment_summary.csv`             Summary statistics for each
                                        populated RFM segment.
  -------------------------------------------------------------------------
