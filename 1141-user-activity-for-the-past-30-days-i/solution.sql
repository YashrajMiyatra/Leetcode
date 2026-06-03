-- 100th Percentile SARGable B-Tree Range Engine
-- 
-- Architecture:
-- - **Theoretical Foundation**: The problem requires counting active users specifically over a 30-day sliding window 
--   ending exactly on `'2019-07-27'`.
-- - **Execution**: A standard and highly unoptimized developer instinct is to evaluate time using dynamic Date functions 
--   like `DATEDIFF('2019-07-27', activity_date) BETWEEN 0 AND 29`. 
--   Applying *any* scalar function (`DATEDIFF`) on a database column forcefully destroys SARGability. The Query Optimizer 
--   goes completely blind, abandons the `B+ Tree` index on `activity_date`, and executes a Full Table Scan computing date 
--   subtractions on millions of rows sequentially.
--   
--   To literally crush the execution time to bare metal IO limits, I explicitly hard-coded the exact pre-calculated date limits 
--   (`2019-06-28` to `2019-07-27`). This leaves the column `activity_date` entirely bare, allowing the SQL Optimizer to trigger 
--   an instantaneous `Index Range Scan`. The database physically jumps straight to `2019-06-28` in the `B-Tree` and horizontally 
--   streams the block chunks to the aggregate hash map!

SELECT 
    activity_date AS day, 
    COUNT(DISTINCT user_id) AS active_users
FROM Activity
WHERE activity_date BETWEEN '2019-06-28' AND '2019-07-27'
GROUP BY activity_date;
