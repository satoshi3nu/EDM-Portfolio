# Finals Lab Task 1: MySQL Basics

## Task Description:
Task 1: Create a table named `employees` with the following fields:
`employee_id: Unique integer, auto_increment, primary key`
`employee_name: string (varchar) with up to 255 characters, not null`
`manager_id: integer, foreign key referencing employee_id in the same table (employees)`

Task 2: Create a table named `departments` with the following fields:
`department_id: Unique integer, auto_increment, primary key`
`department_name: string (varchar) with up to 255 characters, not null`

Task 3: Create a table named `employee_departments` with the following fields:
`employee_id: integer, foreign key referencing employee_id in employees`
`department_id: integer, foreign key referencing department_id in departments`
`Composite primary key (employee_id, department_id)`

Task 4: Create a table named `employee_projects` with the following fields:
`employee_id: integer, foreign key referencing employee_id in employees`
`project name: String (VARCHAR) with up to 255  characters, NOT NULL`

Task 5: Create a table named `managers` with the following fields:
`manager_id: Unique integer, auto_increment, primary key`
`employee_id: integer, foreign key referencing employee_id in employees`

## REQUIRED OUTPUT
1. Query statements (Task 1-5)
2. Table Structure (Task 1-5)
3. And 1 ER Diagram or Relational schema from phpMyAdmin or Workbench (pdf or jpg file)
4. Sql copy of the database and table sturctures

## STEP 1:
- Open XAMPP and start the Apatche and MySQL
- Launch MySQL Workbench on your computer
- Connect to your MySQL server
- If it's your first time using MySQL Workbench, create a new connection (enter credentials like hostname, username, password, etc.).

## STEP 2:
- In the MySQL Workbench main window, click on the + icon next to "Schemas" (on the left panel)
- In the new tab, type the following SQL command to create a new database (`CREATE DATABASE multi_level_company;` & `USE multi_level_company;`)
- Click "Execute" to execute the command

## TASK 1
CODE: `CREATE TABLE employees (employee_id INT AUTO_INCREMENT PRIMARY KEY, employee_name VARCHAR(255) NOT NULL, manager_id INT, FOREIGN KEY (manager_id) REFERENCES employees(employee_id));`
#### QUERY STATEMENT & TABLE STRUCTURE
![employees_table](Image%20%26%20File/employees_tbl.jpg)

## TASK 2
CODE: `CREATE TABLE departments (department_id INT AUTO_INCREMENT PRIMARY KEY, department_name VARCHAR(255) NOT NULL);`
#### QUERY STATEMENT & TABLE STRUCTURE
![departments_table](Image%20%26%20File/departments_tbl.jpg)


## TASK 3
CODE: `CREATE TABLE employee_departments (
    employee_id INT,
    department_id INT,
    PRIMARY KEY (employee_id, department_id),
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id),
    FOREIGN KEY (department_id) REFERENCES departments(department_id)
);`
#### QUERY STATEMENT & TABLE STRUCTURE
![employee_departments_table](Image%20%26%20File/employee_departments_tbl.jpg)

## TASK 4
CODE: `CREATE TABLE employee_projects (employee_id INT, project_name VARCHAR(255) NOT NULL, FOREIGN KEY (employee_id) REFERENCES employees(employee_id));`
#### QUERY STATEMENT & TABLE STRUCTURE
![employee_projects_table](Image%20%26%20File/employee_projects_tbl.jpg)

## TASK 5
CODE: `CREATE TABLE managers (manager_id INT AUTO_INCREMENT PRIMARY KEY, employee_id INT, FOREIGN KEY (employee_id) REFERENCES employees(employee_id));`
#### QUERY STATEMENT & TABLE STRUCTURE
![managers_table](Image%20%26%20File/managers_tbl.jpg)

## HERE IS THE ER Diagram OR Relational schema
![](Image%20%26%20File/ER%20Diagram.jpg)

## HERE IS MYSQL FILE
 [Database.SQL](Image%20%26%20File/Database.sql)
 
 [employees_Table.SQL](Image%20%26%20File/employees_tbl.sql)

 [departments_Table.SQL](Image%20%26%20File/departments_tbl.sql)

 [employee_departments_Table.SQL](Image%20%26%20File/employee_departments_tbl.sql)

 [employee_projects_Table.SQL](Image%20%26%20File/employee_projects_tbl.sql)

 [managers_Table.SQL](Image%20%26%20File/managers_tbl.sql)
