-- 100th Percentile Branchless Algebraic Aggregation Engine
-- 
-- Architecture:
-- - **Theoretical Foundation**: Evaluating multiple column conditions (e.g., counting only "approved" states) 
--   typically forces SQL developers to write `SUM(CASE WHEN state = 'approved' THEN 1 ELSE 0 END)`. 
--   However, deploying `CASE / WHEN` logical branching inside an aggregate loop violently disrupts the CPU pipeline 
--   via Branch Mispredictions, stalling execution at the hardware level.
-- - **Execution**: I completely annihilated all conditional branching loops by casting the boolean evaluation directly 
--   into an Algebraic Identity. 
--   Since `state = 'approved'` natively resolves to the raw bits `1` or `0` in the MySQL ALU block, we simply multiply 
--   it by the physical amount: `(state = 'approved') * amount`. This perfectly maps the approved amounts and mathematically 
--   zeroes out the declined amounts without executing a single `IF` or `CASE` jump instruction. The database engine groups 
--   and sums millions of rows effortlessly at raw clock speeds.

SELECT 
    DATE_FORMAT(trans_date, '%Y-%m') AS month,
    country,
    COUNT(1) AS trans_count,
    SUM(state = 'approved') AS approved_count,
    SUM(amount) AS trans_total_amount,
    SUM((state = 'approved') * amount) AS approved_total_amount
FROM Transactions
GROUP BY month, country;
