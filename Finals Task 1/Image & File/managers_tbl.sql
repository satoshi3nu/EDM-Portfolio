CREATE TABLE managers (manager_id INT AUTO_INCREMENT PRIMARY KEY, employee_id INT, FOREIGN KEY (employee_id) REFERENCES employees(employee_id));
DESCRIBE managers;