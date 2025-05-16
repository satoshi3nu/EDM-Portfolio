--DEMO codes using SQL views and stored procedures:

use hrd;
--Example 1 CREATE a VIEW 
CREATE VIEW employee_attendance AS 
SELECT first_name, last_name
FROM employees;

--Example 2 UPDATE a VIEW 
UPDATE employee_attendance SET first_name= 'Khaa' WHERE last_name='Khoo';
--Check the updates
SELECT *from employees WHERE last_name='Khoo';
--DELETE a VIEW
DROP VIEW employee_attendance;

--SAMPLE STORED PROCEDURES
--Example 1
DELIMITER $$
CREATE PROCEDURE get_employees()
BEGIN
 SELECT * FROM employees;
END $$
DELIMITER ;

CALL get_employees();

DROP PROCEDURE get_customers;

--Example 2 with 1 parameter
DELIMITER $$
CREATE PROCEDURE find_employee(IN id INT)  
BEGIN  
 SELECT *
 FROM employees
 WHERE employee_id = id;
END $$
DELIMITER ; 

CALL find_employee(100)

--Example 3 Stored Procedure with 2 parameters--

DELIMITER $$
CREATE PROCEDURE find_employees(IN f_name VARCHAR(50),IN l_name VARCHAR(50))  
BEGIN  
 SELECT *
 FROM employees
 WHERE first_name = f_name AND last_name = l_name;
END $$
DELIMITER ;

CALL find_employees("Khaa","Khoo")




--AGGREGATE functions

FUNCTIONS


SELECT COUNT(amount) as count
FROM transactions;

SELECT MAX(amount) AS maximum
FROM transactions;

SELECT MIN(amount) AS minimum
FROM transactions;

SELECT AVG(amount) AS average
FROM transactions;

SELECT SUM(amount) AS sum
FROM transactions;

SELECT CONCAT(first_name, “ ”, last_name) AS full_name
FROM employees;