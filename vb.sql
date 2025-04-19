-- Create a sample table called 'employees'
CREATE TABLE employees (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    salary DECIMAL(10, 2),
    department VARCHAR(50)
);

-- Insert some sample data into the 'employees' table
INSERT INTO employees (id, name, salary, department)
VALUES
(1, 'Alice', 60000, 'HR'),
(2, 'Bob', 75000, 'Finance'),
(3, 'Charlie', 50000, 'IT'),
(4, 'David', 80000, 'Finance'),
(5, 'Eve', 55000, 'HR'),
(6, 'Frank', 95000, 'IT'),
(7, 'Grace', 120000, 'Finance');

-- Demonstrate the use of aggregate functions

-- COUNT() - Count the number of rows in the 'employees' table
SELECT COUNT(*) AS TotalEmployees FROM employees;

-- SUM() - Calculate the total sum of salaries
SELECT SUM(salary) AS TotalSalary FROM employees;

-- AVG() - Calculate the average salary
SELECT AVG(salary) AS AverageSalary FROM employees;

-- MIN() - Get the minimum salary
SELECT MIN(salary) AS MinSalary FROM employees;

-- MAX() - Get the maximum salary
SELECT MAX(salary) AS MaxSalary FROM employees;

-- GROUP_CONCAT() or STRING_AGG() (MySQL example)
-- Concatenate all employee names into a single string (this is specific to MySQL)
SELECT GROUP_CONCAT(name ORDER BY name SEPARATOR ', ') AS EmployeeNames
FROM employees;

-- Variance (if supported by your DBMS, e.g., PostgreSQL, SQL Server, Oracle)
SELECT VARIANCE(salary) AS SalaryVariance FROM employees;

-- Standard Deviation (if supported)
SELECT STDDEV(salary) AS SalaryStdDev FROM employees;

-- GROUP BY with aggregate functions (e.g., Grouping by department)
SELECT department, 
       COUNT(*) AS EmployeeCount, 
       AVG(salary) AS AverageSalary, 
       MAX(salary) AS MaxSalary
FROM employees
GROUP BY department;

