-- 1. Create Tables with Constraints

CREATE TABLE Students (
    student_id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

CREATE TABLE Courses (
    course_id INT PRIMARY KEY,
    course_name VARCHAR(100) NOT NULL
);

CREATE TABLE Enrollments (
    student_id INT,
    course_id INT,
    PRIMARY KEY (student_id, course_id),
    FOREIGN KEY (student_id) REFERENCES Students(student_id),
    FOREIGN KEY (course_id) REFERENCES Courses(course_id)
);

-- 2. Insert Sample Data

INSERT INTO Students (student_id, name) VALUES 
(1, 'Alice'), (2, 'Bob'), (3, 'Charlie');

INSERT INTO Courses (course_id, course_name) VALUES 
(101, 'Mathematics'), (102, 'Physics'), (103, 'History');

INSERT INTO Enrollments (student_id, course_id) VALUES 
(1, 101), (1, 102),
(2, 101),
(3, 103);

-- 3. Queries to Get Results

-- Query 1: Find all students enrolled in 'Mathematics'
SELECT s.name
FROM Students s
JOIN Enrollments e ON s.student_id = e.student_id
JOIN Courses c ON e.course_id = c.course_id
WHERE c.course_name = 'Mathematics';

-- Query 2: List total number of courses each student is taking
SELECT s.name, COUNT(e.course_id) AS course_count
FROM Students s
LEFT JOIN Enrollments e ON s.student_id = e.student_id
GROUP BY s.name;
