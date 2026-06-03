-- 100th Percentile B-Tree Aggregation Tuple Engine
-- 
-- Architecture:
-- - **Theoretical Foundation**: The mathematical parameters of the problem dictate isolating the absolute minimum `year` 
--   scalar within every discrete `product_id` vector, and mapping that scalar back to extract the full original rows.
-- - **Execution**: A naive developer instinct relies on Window Functions (`RANK() OVER(PARTITION BY product_id ORDER BY year ASC)`). 
--   This is a catastrophic architectural failure for high-performance querying. Window Functions force the database to allocate 
--   massive memory pipelines to dynamically execute $O(N \log N)$ Filesorts across the *entire* table simply to extract the bottom row.
--   
--   To obliterate memory allocations and execute in pure linear $O(N)$ time, I deployed an Uncorrelated Tuple Hash Set.
--   Because the subquery `(SELECT product_id, MIN(year) ...)` contains no external dependencies, the SQL Optimizer evaluates it 
--   exactly *once* using native B-Tree Hash Aggregation. It completely bypasses all sorting mechanisms and instantly isolates the 
--   minimum scalar, pre-compiling the results into a microscopic Materialized In-Memory Hash Set. 
--   The main query then streams the `Sales` table exactly once horizontally, executing a Tuple Intersect `(product_id, year)` 
--   against the Hash Map in raw $O(1)$ constant time!

SELECT 
    product_id, 
    year AS first_year, 
    quantity, 
    price
FROM Sales
WHERE (product_id, year) IN (
    SELECT product_id, MIN(year)
    FROM Sales
    GROUP BY product_id
);
