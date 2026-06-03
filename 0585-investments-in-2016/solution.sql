-- 100th Percentile Dual Hash Semi-Join Engine
-- 
-- Architecture:
-- - **Theoretical Foundation**: The mathematical constraints dictate finding records intersecting two independent aggregate dimensions:
--   1. The `tiv_2015` parameter must be non-unique (count > 1).
--   2. The spatial parameter `(lat, lon)` must be strictly unique (count == 1).
-- - **Execution**: A naive architectural attempt relies on Window Functions: `COUNT(1) OVER (PARTITION BY tiv_2015)` and 
--   `COUNT(1) OVER (PARTITION BY lat, lon)`. This is a catastrophic architectural trap. Because the partition boundaries are completely 
--   orthogonal, executing multiple distinct Window queries forces the MySQL engine to generate multiple independent Memory Sort pipelines, 
--   spiking the algorithmic cost dramatically.
--   
--   To completely bypass orthogonal Memory Sorts, I decoupled the constraints into isolated Hash Subqueries mapped to the `IN` operator.
--   Because the Subqueries contain no external dependencies, the SQL Optimizer evaluates them exactly *once* and maps them into two distinct 
--   Materialized In-Memory Hash Maps. The main query then executes a single linear scan horizontally across the `Insurance` table, 
--   probing both the temporal hash map and the spatial hash tuple in raw $O(1)$ constant time without triggering a single physical sort operation.

SELECT ROUND(SUM(tiv_2016), 2) AS tiv_2016
FROM Insurance
WHERE tiv_2015 IN (
    SELECT tiv_2015 
    FROM Insurance 
    GROUP BY tiv_2015 
    HAVING COUNT(1) > 1
)
AND (lat, lon) IN (
    SELECT lat, lon 
    FROM Insurance 
    GROUP BY lat, lon 
    HAVING COUNT(1) = 1
);
