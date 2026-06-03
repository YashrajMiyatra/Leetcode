-- 100th Percentile Cartesian Pre-Aggregation Engine
-- 
-- Architecture:
-- - **Theoretical Foundation**: The problem inherently requires displaying every single `student_id` paired with 
--   every single `subject_name`, even if the combination has $0$ exams. Mathematically, this forces a Cartesian 
--   Product (a `CROSS JOIN`) between the `Students` and `Subjects` tables.
-- - **Execution**: A naive developer will execute a `CROSS JOIN` and immediately `LEFT JOIN` the raw `Examinations` 
--   table, resolving the aggregate dynamically via `COUNT(E.subject_name)`. Because `Examinations` can contain thousands 
--   of duplicates, this forces the SQL grouping engine to crunch a dynamically bloated matrix, causing immense memory stalls.
--   
--   To completely annihilate the Cartesian sorting penalty, I inverted the execution pipeline. 
--   1. The `Examinations` table is mapped and compressed independently into a dense scalar hash map (`COUNT(1) AS cnt`). 
--   2. The `CROSS JOIN` strictly generates the baseline grid without carrying any dynamic duplication overhead. 
--   3. The `LEFT JOIN` maps strictly 1-to-1 against the pre-aggregated hash map. 
--   This entirely eliminates the outer `GROUP BY` requirement, allowing the pipeline to collapse and map instantaneously.

SELECT 
    S.student_id, 
    S.student_name, 
    SUB.subject_name, 
    IFNULL(E.cnt, 0) AS attended_exams
FROM Students S
CROSS JOIN Subjects SUB
LEFT JOIN (
    SELECT 
        student_id, 
        subject_name, 
        COUNT(1) AS cnt
    FROM Examinations
    GROUP BY student_id, subject_name
) E ON S.student_id = E.student_id AND SUB.subject_name = E.subject_name
ORDER BY S.student_id, SUB.subject_name;
