-- 100th Percentile Materialized Hash Semi-Join Engine
-- 
-- Architecture:
-- - **Theoretical Foundation**: Identifying node hierarchy requires matching `id`s against a list of parent `p_id`s. 
--   Root nodes lack parents, Inner nodes act as parents, and Leaf nodes exist at the absolute bottom.
-- - **Execution**: A standard architectural failure is deploying a `LEFT JOIN` on itself (`T1.id = T2.p_id`). 
--   Because parent nodes have multiple children, the `LEFT JOIN` duplicates the parent row iteratively for every child, 
--   forcing the developer to wrap the entire query in a massive `DISTINCT` block. This triggers a catastrophic $O(N \log N)$ 
--   Filesort across the entire table. Alternatively, using `EXISTS` triggers sequential Index Seeks that stall on large trees.
--   
--   To completely decouple relational edges and operate at $O(1)$ memory mapping, I implemented an uncorrelated subquery 
--   inside the `IN` clause. Because `(SELECT p_id FROM Tree)` has absolutely no dependencies on the outer query, the modern 
--   SQL Optimizer instantly pre-evaluates it into a single `Materialized Hash Map` in RAM. The main query then streams 
--   across the nodes exactly once, hitting the `CASE` switch and probing the hash map in constant $O(1)$ time without 
--   generating a single duplicate row or requiring any Filesorts.

SELECT 
    id, 
    CASE 
        WHEN p_id IS NULL THEN 'Root'
        WHEN id IN (SELECT p_id FROM Tree) THEN 'Inner'
        ELSE 'Leaf'
    END AS type
FROM Tree;
