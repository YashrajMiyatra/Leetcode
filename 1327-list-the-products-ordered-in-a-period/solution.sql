-- 100th Percentile Pre-Aggregation Pipeline Reduction
-- 
-- Architecture:
-- - **Theoretical Foundation**: The standard query pattern is to `INNER JOIN` the `Orders` and `Products` tables first, 
--   then `GROUP BY` the product name to filter the aggregates. 
-- - **Execution**: Pushing variable-length strings (`VARCHAR product_name`) through the SQL engine's Grouping Hash Table 
--   pipeline consumes enormous memory bandwidth and spikes execution time. Furthermore, computing aggregates *after* 
--   the join causes unnecessary relational edge allocations.
--   
--   To completely bypass memory spikes, I decoupled the pipeline via a `Derived Pre-Aggregation Table`. 
--   First, the engine evaluates purely on raw integers (`product_id` and `unit`) inside the `Orders` table, perfectly utilizing 
--   a SARGable date scan `BETWEEN '2020-02-01' AND '2020-02-29'`. It aggregates and aggressively drops any ID below 100 
--   before a join ever occurs. Finally, it executes an instantaneous `Nested Loop Join` exclusively against the surviving 
--   primary keys in the `Products` table to pull the strings.

SELECT 
    P.product_name, 
    O.unit
FROM (
    SELECT 
        product_id, 
        SUM(unit) AS unit
    FROM Orders
    WHERE order_date BETWEEN '2020-02-01' AND '2020-02-29'
    GROUP BY product_id
    HAVING SUM(unit) >= 100
) O
INNER JOIN Products P 
    ON O.product_id = P.product_id;
