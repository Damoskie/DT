CREATE TABLE employees (
    id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    age INT,
    department VARCHAR(50)
);
INSERT INTO employees (id, first_name, last_name, age, department)
VALUES
(1, 'John', 'Doe', 29, 'HR'),
(2, 'Jane', 'Smith', 35, 'Finance'),
(3, 'Emily', 'Johnson', 28, 'IT'),
(4, 'Michael', 'Brown', 40, 'Marketing'),
(5, 'Sarah', 'Williams', 25, 'Finance');
SELECT * 
FROM employees
WHERE department = 'Finance';
