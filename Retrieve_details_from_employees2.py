/*You are working on an employee management system using SQLite in Python. An in-memory SQLite database has been set up for you, which includes a predefined table called employees with sample data.
The employees table has been created with the following structure and sample data:

id     first_name     last_name      age     department
1        John            Doe         30          HR
2        Jan            Smith        25        Finance
3        Mike          Johnson       35          IT
4        Emily         Davis         29        Marketing

You are provided with a code snippet that takes user input for the first name's starting letter. Modify this code to execute an SQL query that retrieves the details of all employees whose first name begins with the specified letter. 
Note: If no employee's name exists in the table that starts with the user-specified letter, the program will print "No employees found."
*/

import sqlite3
connection=sqlite3.connect(':memory:')
cursor.execute('''CREATE TABLE employees(id INTEGER PRIMARY KEY AUTOINCREMENT,first_name TEXT NOT NULL,
last_name TEXT NOT NULL, age INTEGER, department TEXT)''')
sample_employees=[(1, 'John' ,'Doe' ,30,'HR'),(2,'Jane','Smith',25,'Finance'),(3,'Mike','Johnson',35,'IT'),
                  (4,'Emily','Davis',29,'Marketing')]
cursor.executemany('''INSERT INTO employees(id,first_name,last_name,age,department) VALUES(?,?,?,?,?)''',sample_employees)
connection.commit()
letter=input.strip()
cursor.execute("Select * from employees where first_name like ?",(letter+'%',))
employee_with_letter=cursor.fetchall()
if employees_with_letter:
  for emp in employees_with_letter:
    print(emp)
else:
  print("No employees found")
connection.close()
