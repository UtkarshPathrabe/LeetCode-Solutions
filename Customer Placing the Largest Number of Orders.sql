# Write your MySQL query statement below
SELECT customer_number 
FROM Orders 
GROUP BY customer_number 
ORDER BY Count(*) DESC
LIMIT 1