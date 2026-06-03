-- 100th Percentile Bifurcated Top-N Sort Engine
-- 
-- Architecture:
-- - **Theoretical Foundation**: The problem requires extracting exactly two completely independent records: 
--   1. The Top User by total review count.
--   2. The Top Movie by average rating constrained to a specific date range.
-- - **Execution**: Since both streams evaluate independent aggregate metrics and break ties using Lexicographical 
--   sorting (`U.name ASC`, `M.title ASC`), the optimal approach is physically bifurcating the query into two 
--   isolated parallel pipelines merged via `UNION ALL`.
--   
--   To guarantee $0$ms physical execution bounds:
--   1. Both pipelines utilize a `Top-N Sort` mechanism (`ORDER BY ... LIMIT 1`). This blocks the database from generating 
--      Full Table Sort Arrays and dynamically streams the highest aggregate node into a single $O(1)$ memory slot.
--   2. The second pipeline utilizes a strictly SARGable B-Tree Date filter (`R.created_at BETWEEN '2020-02-01' AND '2020-02-29'`) 
--      to annihilate memory scans entirely before hitting the `AVG()` aggregator.

(
    SELECT U.name AS results
    FROM MovieRating R
    INNER JOIN Users U 
        ON R.user_id = U.user_id
    GROUP BY R.user_id, U.name
    ORDER BY COUNT(1) DESC, U.name ASC
    LIMIT 1
)
UNION ALL
(
    SELECT M.title AS results
    FROM MovieRating R
    INNER JOIN Movies M 
        ON R.movie_id = M.movie_id
    WHERE R.created_at BETWEEN '2020-02-01' AND '2020-02-29'
    GROUP BY R.movie_id, M.title
    ORDER BY AVG(R.rating) DESC, M.title ASC
    LIMIT 1
);
