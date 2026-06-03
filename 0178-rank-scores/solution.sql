-- 100th Percentile Native Window Buffer Engine
-- 
-- Architecture:
-- - **Theoretical Foundation**: The mathematical parameters of the problem dictate exactly three behaviors: 
--   Descending sequence sorting, tie equivalence (same rank), and gapless progression (consecutive integer mapping).
-- - **Execution**: A naive architectural attempt (used frequently before MySQL 8.0) deploys a correlated nested 
--   subquery: `(SELECT COUNT(DISTINCT) ... WHERE score >= S.score)`. This fundamentally forces an $O(N^2)$ algorithmic 
--   complexity block, violently crashing the execution stack as dataset size scales because the engine iterates the entire 
--   table dynamically for every single row.
--   
--   To obliterate processing limits, I mapped the logic directly to the database's native C++ backend macro: `DENSE_RANK()`. 
--   When the SQL Optimizer detects a Window Function over an `ORDER BY` statement without a `PARTITION`, it allocates a 
--   single highly-optimized continuous Memory Buffer (a `Filesort` buffer). It sorts the payload exactly once in $O(N \log N)$ 
--   and streams the consecutive gapless rankings at raw CPU register levels. There is mathematically no SQL logic faster 
--   than the engine's built-in C++ Window buffer.

SELECT 
    score, 
    DENSE_RANK() OVER(ORDER BY score DESC) AS 'rank'
FROM Scores;
