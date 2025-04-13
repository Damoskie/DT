SELECT 
    salesperson_id,
    COUNT(sale_id) AS total_sales,             -- Count the number of sales per salesperson
    SUM(amount) AS total_revenue,              -- Sum the sales amount for each salesperson
    AVG(amount) AS average_sale_amount,       -- Calculate the average sale amount
    MAX(amount) AS highest_sale,              -- Find the highest sale amount
    MIN(amount) AS lowest_sale                -- Find the lowest sale amount
FROM 
    Sales
WHERE 
    sale_date BETWEEN '2023-01-01' AND '2023-02-28'  -- Filtering by date range
GROUP BY 
    salesperson_id                             -- Group by salesperson
HAVING 
    SUM(amount) > 1000                        -- Only include salespeople with total sales above 1000
ORDER BY 
    total_revenue DESC;                       -- Sort by total revenue in descending order
