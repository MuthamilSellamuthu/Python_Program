/* 4. Write a program that takes a string as input and prints the total count of vowels in that string. Consider both uppercase and lowercase.

Input Format:
A single line contains a string that may contain letters, numbers, and punctuation.

Output Format:
An integer representing the total number of vowels in the input string.
*/

str=input()
count=0
v=['a','e','i','o','u','A','E','I','O','U']
for i in str:
  if i in v:
    count+=1
print(count)
