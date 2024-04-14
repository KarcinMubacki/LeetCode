# Write your MySQL query statement below
SELECT name FROM Customer
WHERE referee_id IS NULL or NOT (referee_id = 2) 