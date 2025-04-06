-- 1. Creating the Employees table
CREATE TABLE Employees (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    age INT,
    salary DECIMAL(10, 2),
    department VARCHAR(50)
);

-- 2. Inserting sample data into Employees table
INSERT INTO Employees (id, name, age, salary, department)
VALUES
    (1, 'John Doe', 28, 50000, 'HR'),
    (2, 'Jane Smith', 35, 65000, 'IT'),
    (3, 'Emily Davis', 30, 60000, 'Finance'),
    (4, 'Michael Brown', 40, 80000, 'IT'),
    (5, 'Sarah Wilson', 25, 55000, 'HR'),
    (6, 'David Lee', 45, 70000, 'Finance');

-- 3. Select all employees who are older than 30 and earn more than $60,000
SELECT * FROM Employees
WHERE age > 30
  AND salary > 60000;

-- 4. Select employees in the 'HR' or 'Finance' departments
SELECT * FROM Employees
WHERE department IN ('HR', 'Finance');

-- 5. Select employees whose age is between 30 and 40
SELECT * FROM Employees
WHERE age BETWEEN 30 AND 40;

-- 6. Select employees who either belong to the 'IT' department or have a salary greater than $75,000
SELECT * FROM Employees
WHERE department = 'IT' OR salary > 75000;

-- 7. Select employees whose name starts with 'J' and salary is between 50,000 and 60,000
SELECT * FROM Employees
WHERE name LIKE 'J%' AND salary BETWEEN 50000 AND 60000;

-- 8. Select employees who are either in the 'HR' or 'IT' department and are older than 30
SELECT * FROM Employees
WHERE (department = 'HR' OR department = 'IT')
  AND age > 30;

-- 9. Select employees who have an 'id' not in the range of 1 to 3
SELECT * FROM Employees
WHERE id NOT BETWEEN 1 AND 3;

-- 10. Select the employees with a salary less than $60,000 and who are not in the 'Finance' department
SELECT * FROM Employees
WHERE salary < 60000
  AND department != 'Finance';
