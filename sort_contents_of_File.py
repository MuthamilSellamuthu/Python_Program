/*
10. Develop a program to sort the contents of a text file and write the sorted contents into a separate text file and print the output.
[Hint: Use string methods strip(), len(), list methods sort(), append(), and file methods open(), read lines(), and write()].

Note: The output file should have only lower-case words, so any upper-case words from source must be lowered. 
Note:Refer to shown test cases to match with the input and output format.
*/

fn=input()
try:
  fr=open(fn,"r")
  line=fr.readlines()
  word=[i.strip().lower() for i in line]
  word.sort()
  for i in word:
    print(i)
except FileNotFoundError:
  print("File not found")
