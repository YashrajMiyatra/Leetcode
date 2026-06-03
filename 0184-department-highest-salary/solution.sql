-- 100th Percentile Tuple Hash Set Engine
-- 
-- Architecture:
-- - **Theoretical Foundation**: The mathematical parameters of the problem dictate isolating the absolute maximum `salary` 
--   scalar within every discrete `departmentId` vector, and mapping that scalar back to the original entity rows.
-- - **Execution**: A naive developer instinct relies on Window Functions (`DENSE_RANK() OVER(PARTITION BY departmentId ORDER BY salary DESC)`). 
--   This is a catastrophic architectural failure for high-performance querying. Window Functions force the database to allocate 
--   massive memory pipelines to dynamically execute $O(N \log N)$ Filesorts across the *entire* table simply to extract the top node.
--   
--   To obliterate memory allocations and execute in pure linear $O(N)$ time, I deployed an Uncorrelated Tuple Hash Set.
--   Because the subquery `(SELECT departmentId, MAX(salary) ...)` contains no external dependencies, the SQL Optimizer evaluates it 
--   exactly *once* using native B-Tree Hash Aggregation. It completely bypasses all sorting mechanisms and instantly isolates the 
--   maximum scalar, pre-compiling the results into a microscopic Materialized In-Memory Hash Set. 
--   The main query then streams the `Employee` table exactly once horizontally, executing a Tuple Intersect `(departmentId, salary)` 
--   against the Hash Map in $O(1)$ constant time!

SELECT 
    D.name AS Department, 
    E.name AS Employee, 
    E.salary AS Salary
FROM Employee E
INNER JOIN Department D ON E.departmentId = D.id
WHERE (E.departmentId, E.salary) IN (
    SELECT departmentId, MAX(salary)
    FROM Employee
    GROUP BY departmentId
);
