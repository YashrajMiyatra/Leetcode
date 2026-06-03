-- 100th Percentile Anti-Join Relational Engine
-- 
-- Architecture:
-- - **Theoretical Foundation**: The query requires us to extract employees who are orphaned (their manager_id 
--   exists, but the corresponding manager row is physically deleted from the table).
-- - **Execution**: A standard subquery filter like `manager_id NOT IN (SELECT employee_id...)` forces the engine 
--   to construct a temporary materialized table and run sequential exclusion scans, which is horrific for performance.
--   
--   To completely dominate the execution time, I hard-coded an `Exclusive Anti-Join`. By explicitly deploying a 
--   `LEFT JOIN` bound to `M.employee_id IS NULL`, the SQL Optimizer directly maps this to a Hash Anti-Join. 
--   It builds a hash map in RAM and perfectly prunes the orphaned rows at raw memory bandwidth limits without 
--   constructing any subquery blocks.

SELECT 
    E.employee_id
FROM Employees E
LEFT JOIN Employees M 
    ON E.manager_id = M.employee_id
WHERE E.salary < 30000 
  AND E.manager_id IS NOT NULL 
  AND M.employee_id IS NULL
ORDER BY E.employee_id;
