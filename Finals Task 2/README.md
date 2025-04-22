# Finals Lab Task 2: Transforming ER Model to Relational Tables

## Task Description: 
Given the ER diagram representing student assignment submissions, convert it into MySQL
tables. Capture all entities and their attributes, and define the relationships between students,
submissions, and assignments. Identify the primary and foreign keys and ensure proper
representation of any dependent or weak entities.

![ER model](Image%20%26%20File/Model.jpg)

## REQUIRED OUTPUT
1. Query statements (Task 1-4 including the table relationship)
2. Table Structure (Task 1- 4 including the table relationship)
3. ER Diagram or Relational schema from phpMyAdmin or Workbench (pdf or jpg file)
4. Sql copy of the database and table structures
   
 * Note: Create the appropriate table relationship and enforce necessary REFERENTIAL INTEGRITY CONSTRAINTS

## STEP 1:
- Open XAMPP and start the Apatche and MySQL
- Launch MySQL Workbench on your computer
- Connect to your MySQL server
- If it's your first time using MySQL Workbench, create a new connection (enter credentials like hostname, username, password, etc.).
  
## STEP 2:
- In the MySQL Workbench main window, click on the + icon next to "Schemas" (on the left panel)
- In the new tab, type the following SQL command to create a new database (`CREATE DATABASE student_submission_db;` & `USE student_submission_db;`)
- Click "Execute" to execute the command

## Creating Tables Instruction
* student table:
`username: string(varchar), up to 50 characters`

* assignment table:
`shortname: string(varchar), up to 50 characters`
`due_date: Date, Cannot be null`
`url: string(varchar), up to 50 characters, can be null`

* submission table:
`username: string(varchar), up to 50 characters`
`shortname: string(varchar), up to 50 characters`
`version: integer, represent the version of the submission`
`submit_date: date, cannot be null`
`data: text`

## Creating Table

1. Creating Student Table
  
`CREATE TABLE student (studentusername VARCHAR(50) PRIMARY KEY);`
#### TABLE STRUCTURE
![Student Table](Image%20%26%20File/student_tbl.jpg)

2. Creating Assignment Table

` CREATE TABLE assignment (shortname VARCHAR(50) PRIMARY KEY, due_date DATE NOT NULL, url VARCHAR(50)); `
#### TABLE STRUCTURE
![Assignment Table](Image%20%26%20File/assignment_tbl.jpg)

3. Creating Submission Table
  
`CREATE TABLE submission (
    username VARCHAR(50),
    shortname VARCHAR(50),
    version INT,
    submit_date DATE NOT NULL,
    data TEXT,
    PRIMARY KEY (username, shortname, version),
    FOREIGN KEY (username) REFERENCES student(username)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (shortname) REFERENCES assignment(shortname)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);`
#### TABLE STRUCTURE
![Submission Table](Image%20%26%20File/submission_tbl.jpg)

### HERE IS THE ER Diagram OR Relational schema
![](Image%20%26%20File/ER%20Diagram.jpg)


#### HERE IS MYSQL FILE
 [Student_Table.SQL](Image%20%26%20File/student_tbl.sql)
 
 [Assignment_Table.SQL](Image%20%26%20File/assignment_tbl.sql)
 
 [Submission_Table.SQL](Image%20%26%20File/submission_tbl.sql)
