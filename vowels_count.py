/* 4. Write a program that takes a string as input and prints the total count of vowels in that string. Consider both uppercase and lowercase.

Input Format:
A single line contains a string that may contain letters, numbers, and punctuation.

Output Format:
An integer representing the total number of vowels in the input string.
*/

str=input()
count=0
for i in str:
  if i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U':
    count+=1
print(count)
