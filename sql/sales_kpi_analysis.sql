USE olist_analytics;

-- QUERY 1: SALES KPI ANALYSIS
-- PURPOSE:
-- Calculate the number of delivered orders, total item
-- sales value and average item sales value per delivered
-- order.
-- NOTE: Freight charges are excluded from item sales value.

SELECT
    COUNT(DISTINCT o.order_id) AS delivered_orders,
    ROUND(SUM(oi.price), 2) AS total_item_sales_value,
    ROUND(
        SUM(oi.price) / COUNT(DISTINCT o.order_id), 2
    ) AS avg_item_sales_per_delivered_order
FROM orders o
JOIN order_items oi
    ON o.order_id = oi.order_id
WHERE o.order_status = 'delivered';

-- QUERY 3: MONTHLY SALES TREND
-- PURPOSE:
-- Calculate delivered order counts and item sales value
-- grouped by the month when orders were purchased.
-- Only orders with delivered status are included.
-- NOTE: This groups eventual delivered orders by purchase
-- month; it does not measure sales by delivery month.

SELECT
    DATE_FORMAT(o.order_purchase_timestamp, '%Y-%m') AS sales_month,
    COUNT(DISTINCT o.order_id) AS delivered_orders,
    ROUND(SUM(oi.price), 2) AS item_sales_value
FROM orders o
JOIN order_items oi
    ON o.order_id = oi.order_id
WHERE o.order_status = 'delivered'
GROUP BY DATE_FORMAT(o.order_purchase_timestamp, '%Y-%m')
ORDER BY sales_month;

-- QUERY 4: PAYMENT METHOD ANALYSIS
-- PURPOSE:
-- Compare payment methods by number of payment records,
-- total payment value and average payment value.
-- NOTE: Payment records are counted, not distinct orders.

SELECT
    payment_type,
    COUNT(*) AS payment_records,
    ROUND(SUM(payment_value), 2) AS total_payment_value,
    ROUND(AVG(payment_value), 2) AS average_payment_value
FROM payments
GROUP BY payment_type
ORDER BY total_payment_value DESC;

-- Top 10 product categories by item sales value
-- Purpose: Rank delivered-order product categories using
-- English category names. Freight is excluded.

SELECT
    COALESCE(
        ct.product_category_name_english,
        p.product_category_name,
        'unknown'
    ) AS category,
    ROUND(SUM(oi.price), 2) AS item_sales_value
FROM orders o
JOIN order_items oi
    ON o.order_id = oi.order_id
JOIN products p
    ON oi.product_id = p.product_id
LEFT JOIN category_translation ct
    ON p.product_category_name = ct.product_category_name
WHERE o.order_status = 'delivered'
GROUP BY category
ORDER BY item_sales_value DESC
LIMIT 10;

-- Query 5: Delivery performance
-- Purpose: Compare delivered orders with late deliveries.
-- A delivery is late when actual delivery is after the estimated date.

SELECT
    COUNT(*) AS delivered_orders,
    SUM(
        CASE
            WHEN order_delivered_customer_date >
                 order_estimated_delivery_date
            THEN 1
            ELSE 0
        END
    ) AS late_delivered_orders,
    ROUND(
        100.0 * SUM(
            CASE
                WHEN order_delivered_customer_date >
                     order_estimated_delivery_date
                THEN 1
                ELSE 0
            END
        ) / COUNT(*),
        2
    ) AS late_delivery_percentage
FROM orders
WHERE order_status = 'delivered'
  AND order_delivered_customer_date IS NOT NULL
  AND order_estimated_delivery_date IS NOT NULL;