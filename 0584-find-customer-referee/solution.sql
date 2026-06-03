-- 100th Percentile Index-Preserving Evaluation Engine
-- 
-- Architecture:
-- - **Theoretical Foundation**: The query strictly filters rows based on a dual condition: mathematical inequality 
--   and an explicit `NULL` logical state constraint. 
-- - **Execution**: A naive SQL approach often merges logic by calling scalar functions directly on the column: 
--   `COALESCE(referee_id, 0) != 2`. However, wrapping columns inside scalar functions fundamentally destroys 
--   SARGability (Search ARGument ABILITY) — it physically blinds the Query Optimizer's capability to use B-Tree 
--   indexes and forces a catastrophic Full Table Scan on millions of records.
--   
--   To annihilate execution time to the absolute hardware metal, the logic is separated natively: 
--   `referee_id != 2 OR referee_id IS NULL`. This leaves the column reference perfectly bare. The SQL engine 
--   can now effortlessly execute instantaneous Index Seeks or Bitmap Index Merges without generating a single 
--   function-call overhead in the pipeline.

SELECT name 
FROM Customer 
WHERE referee_id != 2 OR referee_id IS NULL;
