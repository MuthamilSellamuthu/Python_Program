/*You are working on an employee management system using SQLite in Python. An in-memory SQLite database has been set up for you, which includes a predefined table called employees with sample data.
The employees table has been created with the following structure and sample data:

id     first_name     last_name      age     department
1        John            Doe         30          HR
2        Jan            Smith        25        Finance
3        Mike          Johnson       35          IT
4        Emily         Davis         29        Marketing

You are provided with a code snippet that accepts user input for an employee's age. Modify this code to execute an SQL query that deletes the record of employees whose age matches the specified user input.
*/

import sqlite3
connection=sqlite3.connect(':memory:')
cursor.execute('''CREATE TABLE employees(id INTEGER PRIMARY KEY AUTOINCREMENT,first_name TEXT NOT NULL,
last_name TEXT NOT NULL, age INTEGER, department TEXT)''')
sample_employees=[(1, 'John' ,'Doe' ,30,'HR'),(2,'Jane','Smith',25,'Finance'),(3,'Mike','Johnson',35,'IT'),
                  (4,'Emily','Davis',29,'Marketing')]
cursor.executemany('''INSERT INTO employees(id,first_name,last_name,age,department) VALUES(?,?,?,?,?)''',sample_employees)
connection.commit()
age_to_delete=int(input().strip())

cursor.execute("delete fromemployees where age=?",(age_to_delete,))
connection.commit()

cursor.execute("SELECT * FROM employees")
remaining_employees=cursor.fetchall()
print(f"{'ID':15} {'First Name':<15} {'Last Name':<15} {'Age':<5} {'Department':<15}")
print("="*70)
for employee in remaining_employees:
  print(f"{employee[0]:<5} {employee[1]:<15} {employee[2]:<15} {employee[3]:<5} {employee[4]:<15}")
connection.close()
