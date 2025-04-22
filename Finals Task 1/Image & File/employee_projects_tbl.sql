CREATE TABLE employee_projects (employee_id INT, project_name VARCHAR(255) NOT NULL, FOREIGN KEY (employee_id) REFERENCES employees(employee_id));
DESCRIBE employee_projects;