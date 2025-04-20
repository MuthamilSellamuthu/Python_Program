/* 5. Write a program that takes a string as input and prints the string with the order of the words reversed while keeping the characters in each word in the same order.

Input Format:
A string containing a sentence (words separated by spaces).

Output Format:
A string with the words in reverse order.
*/

str1=input().split()
s="".join(str1[::-1])
print(s)
