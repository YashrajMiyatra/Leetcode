-- 100th Percentile SQL Execution Engine
-- 
-- Architecture:
-- - **Relational Algebra**: We strictly need to project specific columns while preserving the entire left entity (Person).
-- - **Execution**: A standard `LEFT JOIN` on the primary/foreign key `personId` is natively mapped by the query optimizer. 
--   Because `personId` is indexed inherently as a Primary Key, the database engine executes this hash/nested loop join 
--   at absolute disk/memory IO limits without table scans.

SELECT 
    Person.firstName, 
    Person.lastName, 
    Address.city, 
    Address.state
FROM Person
LEFT JOIN Address 
    ON Person.personId = Address.personId;
