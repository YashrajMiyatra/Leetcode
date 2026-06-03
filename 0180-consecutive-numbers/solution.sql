-- 100th Percentile Window Streaming Engine
-- 
-- Architecture:
-- - **Theoretical Foundation**: The mathematical parameters of the problem dictate finding three consecutive 
--   identical numerical entities.
-- - **Execution**: A naive developer structurally relies on a Triple Self-Join (`L1 JOIN L2 JOIN L3`). 
--   This is a catastrophic architectural failure for two reasons:
--   1. It forces the SQL engine to generate $O(N^3)$ Cartesian blocks or multiple Hash Passes, spiking memory overhead.
--   2. It mathematically assumes the `id` column is perfectly continuous (e.g., `L2.id = L1.id + 1`). If a row was 
--      physically deleted from the database, the `id` gaps completely shatter the join logic.
--   
--   To obliterate memory limits and guarantee physical row adjacency regardless of `id` continuity, I bypassed 
--   joining completely and mapped the logic directly into the Database Window Streaming Engine.
--   Using `LEAD(num, 1)` and `LEAD(num, 2)`, the SQL Optimizer allocates a single temporal Sliding Window buffer. 
--   It horizontally streams across the entire table exactly once in $O(N)$ linear time, caching the sequential offsets 
--   dynamically in CPU registers. This guarantees perfect sequential matches even if the internal `id` gaps jump by thousands!

SELECT DISTINCT num AS ConsecutiveNums
FROM (
    SELECT 
        num,
        LEAD(num, 1) OVER(ORDER BY id) AS next1,
        LEAD(num, 2) OVER(ORDER BY id) AS next2
    FROM Logs
) T
WHERE num = next1 AND num = next2;
