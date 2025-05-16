# Finals Lab Task 5: Using SQL views and Stored Procedures and Stored Functions

## Instructions:
1. To have an idea of how SQL views work, kindly read the lecture on SQL views and stored procedures, then you may try the following examples in MySQL Workbench: 
2. Start Xampp and MySQL Workbench – create or start a connection 
4. Open the  [democodes.SQL](Image%20%26%20File/democodes.sql), and you may try executing all the examples using the hrd.sql file
5. AFTER the practice codes…. Perform the required SQL statements of the ff: use [inventory(1).SQL](Image%20%26%20File/inventory%20(1).sql) for this.
6. Print screen the appropriate sql and output per item

## STEP 1:
CREATE A VIEW that will display the vendors_code, vendors name, product description p_indate, of all products with p_indate from 2002 onwards

CODE: `CREATE VIEW vendors_products_2002_onwards AS
SELECT v.V_CODE, v.V_NAME, p.P_DESCRIPT, p.P_INDATE
FROM Products p
JOIN vendors v ON p.V_CODE = v.V_CODE
WHERE p.P_INDATE >= '2002-01-01';`
### OUTPUT: 
![Task 1](Image%20%26%20File/1.jpg)
![Output 1](Image%20%26%20File/Output%201.jpg)
## STEP 2:
CREATE a VIEW that will display all products whose price range is between 100-150

CODE: `CREATE VIEW products_price_range_100_150 AS
SELECT P_CODE, P_DESCRIPT, P_PRICE
FROM Products
WHERE P_PRICE BETWEEN 100 AND 150;`
### OUTPUT: 
![Task 2](Image%20%26%20File/2.jpg)
![Output 2](Image%20%26%20File/Output%202.jpg)
## STEP 3:
Create a VIEW that will COMPUTE for the (TOTAL_PRICE) of ALL PRODUCTS by getting the (P_ONHAND x P_PRICE) Sold by vendors with the following v_code (21344, 23119 and 24288)

CODE: `CREATE VIEW total_price_by_vendor AS
SELECT v.V_CODE, v.V_NAME, p.P_DESCRIPT, (p.P_ONHAND * p.P_PRICE) AS TOTAL_PRICE
FROM Products p
JOIN vendors v ON p.V_CODE = v.V_CODE
WHERE v.V_CODE IN (21344, 23119, 24288);`
### OUTPUT: 
![Task 3](Image%20%26%20File/3.jpg)
![Output 3](Image%20%26%20File/Output%203.jpg)
## STEP 4:
CREATE a STORED PROCEDURE that WILL take a SINGLE PARAMETER and UPDATED the Name of Vendor ‘Bryson,Inc. ’ to ‘Bryson and Co’.

CODE: `DELIMITER $$
CREATE PROCEDURE update_vendor_name(IN old_name VARCHAR(30), IN new_name VARCHAR(30))
BEGIN
    UPDATE vendors
    SET V_NAME = new_name
    WHERE V_NAME = old_name;
END $$
DELIMITER ;`

`CALL update_vendor_name('Bryson,Inc.', 'Bryson and Co');`
### OUTPUT: 
![Task 4](Image%20%26%20File/4.jpg)

## STEP 5:
CREATE A Function that will take 2 parameters(v_code and v_state) and display All the product description and price based on the parameters passed to the function

CODE: `DELIMITER $$
CREATE PROCEDURE get_products_by_vendor_and_state(IN v_code INT, IN v_state VARCHAR(3))
BEGIN
    SELECT p.P_DESCRIPT, p.P_PRICE
    FROM Products p
    JOIN vendors v ON p.V_CODE = v.V_CODE
    WHERE v.V_CODE = v_code AND v.V_STATE = v_state;
END $$
DELIMITER ;`

`CALL get_products_by_vendor_and_state(21344, 'TN');`
### OUTPUT: 
![Task 5](Image%20%26%20File/5.jpg)
![Output 5](Image%20%26%20File/Output%205.jpg)
