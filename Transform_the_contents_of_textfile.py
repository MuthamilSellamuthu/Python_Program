/*
11. Maya wants to transform the content of a text file, making all letters uppercase. She needs a Python program to read the content of the file, convert all letters to uppercase, and print the transformed content. Implement the program to assist Maya in converting all letters of the file content to uppercase.

Input format:
The input is the file name

Output format:
The program prints the content of the file after converting all letters to uppercase.
Note: Always assume that the given file exists.
*/

fn=input()
fr=open(fn,"r")
line=fr.readlines()
word=[i.strip().upper() for in line]
for i in line:
  print(i)
