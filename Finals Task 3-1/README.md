# Finals Lab Task 3-1: Using MYSQL Clause

# Task Instruction
1. Create a database named online_courseDB
2. Use the online_courseDB
3. Copy and paste the initial query then perform the SELECT statements required for each problems in the figure below: (`download:` [online_courses.sql](Image%20%26%20File/online_courses.sql)

# The following are already implemented:
`CREATE TABLE courses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    course_name VARCHAR(255) NOT NULL,
    category VARCHAR(100) NOT NULL,
    enrollment_limit INT NOT NULL,
    students_enrolled INT NOT NULL
);`

`INSERT INTO courses (course_name, category, enrollment_limit, students_enrolled)
VALUES
    ('Data Science', 'Technology', 50, 45),
    ('Graphic Design', 'Arts', 30, 25),
    ('Digital Marketing', 'Business', 40, 35),
    ('Introduction to Python', 'Technology', 100, 90),
    ('Creative Writing', 'Literature', 25, 20),
    ('UX/UI Design', 'Arts', 50, 40),
    ('Project Management', 'Business', 60, 55),
    ('Artificial Intelligence', 'Technology', 50, 48),
    ('Public Speaking', 'Communication', 30, 28),
    ('Photography', 'Arts', 25, 18),
    ('Web Development', 'Technology', 75, 70),
    ('SEO Strategies', 'Business', 30, 29),
    ('Blockchain Basics', 'Technology', 50, 50),
    ('Accounting 101', 'Business', 45, 40),
    ('Film Editing', 'Arts', 35, 33),
    ('Machine Learning', 'Technology', 60, 55),
    ('Speech Writing', 'Communication', 20, 15),
    ('Interior Design', 'Arts', 40, 38),
    ('Leadership Training', 'Business', 50, 48),
    ('Cybersecurity', 'Technology', 70, 65);`
* 20 courses are already present

# The following are the tasks that need to be implemented using MYSQL statement. Make sure to complete them in the order to specified:

## Task 1: Retrieve all courses where students_enrolled is less than the enrollment_limit
* CODE: `SELECT * FROM courses WHERE students_enrolled < enrollment_limit;`
* Query statements & Output of each query:![Task 1](Image%20%26%20File/Task%201.jpg)

## Task 2: Group courses by category and calculate the total number of students enrolled for each category
* CODE: `SELECT category, SUM(students_enrolled) AS total_students_enrolled FROM courses GROUP BY category;`
* Query statements & Output of each query:![Task 2](Image%20%26%20File/Task%202.jpg)

## Task 3: Retrieve the courses that are fully enrolled (students_enrolled = enrollment_limit)
* CODE: `SELECT * FROM courses WHERE students_enrolled = enrollment_limit;`
* Query statements & Output of each query:![Task 3](Image%20%26%20File/Task%203.jpg)

## Task 4: Calculate the total number of students enrolled across all courses
* CODE: `SELECT SUM(students_enrolled) AS total_students_enrolled FROM courses;`
* Query statements & Output of each query:![Task 4](Image%20%26%20File/Task%204.jpg)

## Task 5: Sort courses by students_enrolled in ascending order
* CODE: `SELECT * FROM courses ORDER BY students_enrolled ASC;`
* Query statements & Output of each query:![Task 5](Image%20%26%20File/Task%205.jpg)

# HERE IS MYSQL FILE
 [Database.SQL](Image%20%26%20File/Database.sql)
 
 [Online_Course_Table.SQL](Image%20%26%20File/online_courses_tbl.sql)


