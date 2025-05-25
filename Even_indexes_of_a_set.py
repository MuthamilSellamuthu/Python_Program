/* 
8. Write a Python program to perform the following steps:

Ask the user to enter five integers each on a new line.
Use these integers to create a set and print it.
Convert the set into a list.
Create the list which contains values located at even indexes in the list and print it.
Convert the list back into a set.
Print the final set.


Input format:
The input consists of five integers, each on new line.


Output format:
The first line prints the set
The second line extracts and prints the list containing values at even indexes.
The next line containing converts the list of these values back into a set and prints the resulting as a set.
*/


  
m=int(input())
n=int(input())
o=int(input())
p=int(input())
q=int(input())
a=set([m,n,o,p,q])
print(a)
l=list(a)
l2=l[::2]
print(l2)
print(set(l2))
