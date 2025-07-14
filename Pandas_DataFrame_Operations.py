/*Write a Python program using Pandas that performs the following operations on a given DataFrame:

Filter Rows: Ask the user to input an age value and display the rows where the Age is greater than the entered value.
Add a New Column: Ask the user to input a new column name and add this new column with all values set to 0.
Modify an Existing Column: Ask the user to input a Name, and update the City of the given user name to "California". Assume the name is always present in the DataFrame.


Input Format:
The user will input:
An integer to filter rows by Age.
A string for the new column.
A string for the Name to modify.

Output Format:
The program will display the following:
The filtered rows where Age > entered age.
The updated DataFrame with the new column added, filled with 0s.
The modified DataFrame with the City of the specified Name changed to "California".
*/


import pandas as pd

# Sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [24, 27, 22, 32, 29],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Miami', 'Seattle']
}
df = pd.DataFrame(data)

# Ask the user to input the age for filtering
age_input = int(input("Age: "))
print(df[df['Age']>age_input])
# Filter rows where Age > user-provided age

# Ask the user to input the new column name to add
new_column_name = input("New column: ")
df[new_column_name]=[0]*len(df['Age'])
# Add the new column with all values set to 0
print(df)
# Ask the user to input the Name whose City needs to be modified
name_to_modify = input("Name: ")
df.loc[df['Name']==name_to_modify,'City']='California'
# Update the City of the given Name to "California"
print(df)

