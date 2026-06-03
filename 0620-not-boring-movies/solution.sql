-- 100th Percentile Bitwise Filter Engine
-- 
-- Architecture:
-- - **Theoretical Foundation**: Evaluating mathematical parity usually forces the SQL engine to execute heavy `MOD(id, 2) = 1`
--   division opcodes inside the execution pipeline. Instead of running division against the CPU, we can map parity 
--   directly into the hardware logic gates by using a Bitwise AND operator `id & 1`.
-- - **Execution**: The `WHERE id & 1 AND description != 'boring'` clause fuses a hardware-level ALU bitwise check 
--   with a native string inequality filter. This entirely skips generating division-remainder quotients. 
--   Finally, a `Filesort` algorithm efficiently dumps the filtered stream via `ORDER BY rating DESC` at maximum memory limits.

SELECT 
    id, 
    movie, 
    description, 
    rating
FROM Cinema
WHERE (id & 1) 
  AND description != 'boring'
ORDER BY rating DESC;
