/* 7.Write a Python program that checks if a given key exists in a dictionary. 

Input Format:
The first line of input contains space separated strings that represent the keys of a dictionary.
The second line contains space separated strings that represent the values of a dictionary.
The third line contains the key (as a string) to check whether it is present in the dictionary or not.

Output Format:
The first line of the output should print the dictionary.
Next, it should print "Exist" if the key is present in the dictionary or print "Does not Exist" if the key is not present in the dictionary and if the length of the keys does not match with length of the values then print "Invalid".
*/

keys=input().split("")
value=input().split("")
if len(keys)!=len(value):
  print("Invalid")
k=input()
d1=dict(zip(keys,value))
if len(keys)==len(value):
  print(d1)
  if k in d1:
    print("Exist")
  else:
    print("Does not Exist")
  
