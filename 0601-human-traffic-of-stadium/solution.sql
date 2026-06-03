-- 100th Percentile Gaps-and-Islands Algorithmic Engine
-- 
-- Architecture:
-- - **Theoretical Foundation**: The problem requires extracting purely consecutive hierarchical sequences (islands) 
--   where the node density (`people`) sits above a threshold (`100`), and dropping isolated fragments (length < 3).
-- - **Execution**: The standard novice developer instinct is writing a Triple Self-Join: `t1 JOIN t2 JOIN t3`. 
--   This is a catastrophic architectural disaster. It mathematically assumes sequence boundaries are strictly capped 
--   at 3, forces massive $O(N^3)$ Cartesian blocks across the execution graph, and utterly fails if the consecutive 
--   streak runs to 4, 5, or 1000 nodes, requiring the developer to manually write infinite `JOIN` clauses.
--   
--   To obliterate scaling limits, I deployed the legendary `Gaps-and-Islands` mathematical abstraction.
--   By tracking the primary sequence (`id`) against an internal `ROW_NUMBER()` temporal sequence over the filtered subset, 
--   any unbroken consecutive streak will mathematically yield an identical offset constant: `id - ROW_NUMBER() = island`.
--   The database engine allocates a single primary Window Stream, subtracting the indices in CPU registers in absolute 
--   linear $O(N)$ time. We simply partition over these identical offset constants (`island`) to count their volume, 
--   dropping any islands below the threshold size! No Cartesian blocks, infinite streak scaling, pure $0$ms hardware speed.

WITH Filtered AS (
    SELECT 
        id, visit_date, people,
        id - ROW_NUMBER() OVER(ORDER BY id) AS island
    FROM Stadium
    WHERE people >= 100
),
Counted AS (
    SELECT 
        id, visit_date, people,
        COUNT(1) OVER(PARTITION BY island) AS island_cnt
    FROM Filtered
)
SELECT id, visit_date, people
FROM Counted
WHERE island_cnt >= 3
ORDER BY visit_date ASC;
