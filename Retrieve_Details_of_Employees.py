/*You are working on an employee management system using SQLite in Python. An in-memory SQLite database has been set up for you, which includes a predefined table called employees with sample data.
The employees table has been created with the following structure and sample data:

id     first_name     last_name      age     department
1        John            Doe         30          HR
2        Jan            Smith        25        Finance
3        Mike          Johnson       35          IT
4        Emily         Davis         29        Marketing

The code for taking input for the department name is provided. Your task is to execute an SQL query to retrieve the details of all employees in the user-specified department and display the results.
Note: Assume that the user-specified department is always present in the table.
*/

import sqlite3
connection=sqlite3.connect(':memory:')
cursor=connection.cursor()
cursor.execute('''CREATE TABLE employees (id INTEGER PRIMARY KEY AUTOINCREMENT, first_name TEXT NOT NULL,
last_name TEXT NOT NULL, age INTEGER,departmnet TEXT)''')
sample_employees=[(1,'John','Doe',30,'HR'),(2,'Jane','Smith',25,'Finance'),(3,'Mike','Johnson',35,'IT'),
                  (4,'Emily','Davis',29,'Marketing')]
cursor.executemany('''INSERT INTO employees (id,first_name,last_name,age,department) VALUES(?,?,?,?,?)''',
                   sample_employees)
department_name=input()
cursor.execute("select * from employees where department=?",(department_name,))
employees_in_department=cursor.fetchall()
for emp in employees_in_department:
  print(emp)
