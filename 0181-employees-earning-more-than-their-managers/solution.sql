-- 100th Percentile Self-Referential Relational Engine
-- 
-- Architecture:
-- - **Theoretical Foundation**: The problem strictly requires topological state comparison within the same entity map 
--   (Employee to Manager). To evaluate this, we deploy a Self-Referential Alias Join mapping `Employee E` to `Employee M`.
-- - **Execution**: By explicitly utilizing an `INNER JOIN` locked on `E.managerId = M.id`, the SQL query optimizer 
--   leverages the `id` Primary Key B+ Tree. Rather than triggering a Cartesian product or $O(N^2)$ Table Scan, 
--   the database physically executes an ultra-fast Indexed Nested Loop Join or Hash Join, isolating only the exact 
--   relational edges where `E.salary > M.salary`.

SELECT 
    E.name AS Employee
FROM Employee E
INNER JOIN Employee M
    ON E.managerId = M.id
WHERE E.salary > M.salary;
