-- Total revenue (sum of quantity * price)
SELECT SUM(quantity * price) AS total_revenue
FROM sales;

-- Average quantity sold per sale
SELECT AVG(quantity) AS avg_quantity
FROM sales;

-- Total number of sales
SELECT COUNT(*) AS total_sales
FROM sales;

-- Maximum and minimum sale price
SELECT MAX(price) AS max_price, MIN(price) AS min_price
FROM sales;

-- Grouped aggregate: Total quantity sold per product
SELECT product_name, SUM(quantity) AS total_quantity_sold
FROM sales
GROUP BY product_name;

-- Daily sales summary
SELECT sale_date, COUNT(*) AS number_of_sales, SUM(quantity * price) AS daily_revenue
FROM sales
GROUP BY sale_date
ORDER BY sale_date;
