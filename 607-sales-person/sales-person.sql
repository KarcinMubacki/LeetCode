# Write your MySQL query statement below
SELECT s.name FROM SalesPerson s WHERE s.name NOT IN(
SELECT s.NAME FROM Orders o JOIN SalesPerson s ON o.sales_id = s.sales_id JOIN Company c ON c.com_id = o.com_id
WHERE c.name = "RED" 
)