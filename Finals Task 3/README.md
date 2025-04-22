# Finals Lab Task 3: Table Manipulation

## Task Description:
Task 1: Create a table named `products` with the following fields:
`id: Unique integer, Auto increment, Primary key`
`product_name: string (varchar) with a maximum length of 100, cannot be null`
`price: decimal`

Task 2: Add a `CHECK` constraint to ensure that the price of product must be greater than 0

Task 3: Insert a products that will not violate the check constraint into the products table:
* Product 1: "Laptop", 999.99
* Product 2: "Headphones", -49.99
* Product 3: "Smartphone", 599.99
* Product 4: "Tablet", 299.99
* Product 5: "Monitor", -149.99
* Product 6: "Keyboard", 19.99
* Product 7: "Mouse", 14.99
* Product 8: "Desk Lamp", 24.99
* Product 9: "External Hard Drive", -79.99
* Product 10: "Speakers", 9.99

Task 4: Modify the `product_name` field to have a maximum length of 120 characters

## REQUIRED OUTPUT
1. Query statements (Task 1-4)
2. Table Structure (Task 1-4)
3. ER Diagram or Relational schema from phpMyAdmin or Workbench (pdf or jpg file)
4. Sql copy of the database and table structures

## STEP 1:
- Open XAMPP and start the Apatche and MySQL
- Launch MySQL Workbench on your computer
- Connect to your MySQL server
- If it's your first time using MySQL Workbench, create a new connection (enter credentials like hostname, username, password, etc.).

## STEP 2:
- In the MySQL Workbench main window, click on the + icon next to "Schemas" (on the left panel)
- In the new tab, type the following SQL command to create a new database (`CREATE DATABASE store_db;` & `USE store_db;`)
- Click "Execute" to execute the command

## TASK 1 & 2:
CODE: `CREATE TABLE products (id INT AUTO_INCREMENT PRIMARY KEY, product_name VARCHAR(100) NOT NULL, price DECIMAL(10,2), CHECK (price > 0));`
#### QUERY STATEMENT & TABLE STRUCTURE
![products_table](Image%20%26%20File/Create%20Table.jpg)

## TASK 3:
CODE: `INSERT INTO products (product_name, price) VALUES ('Laptop', 999.99), ('Smartphone', 599.99), ('Tablet', 299.99), ('Keyboard', 19.99), ('Mouse', 14.99), ('Desk Lamp', 24.99), ('Speakers', 9.99);`
#### QUERY STATEMENT & TABLE STRUCTURE
![products_table](Image%20%26%20File/Inserting%20Data.jpg)

## TASK 4:
CODE: `ALTER TABLE products MODIFY product_name VARCHAR(120) NOT NULL;`
#### QUERY STATEMENT & TABLE STRUCTURE
![products_table](Image%20%26%20File/Modify%20Column.jpg)

## HERE IS THE ER Diagram OR Relational schema
![](Image%20%26%20File/ER%20Diagram.jpg)


## HERE IS MYSQL FILE
 [Database.SQL](Image%20%26%20File/Database.sql)
 
 [Products_Table.SQL](Image%20%26%20File/products_tbl.sql)
