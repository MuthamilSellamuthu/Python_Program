/*
9. You are managing a fruit store, and each fruit has a certain price per kilogram. Write a program to create a dictionary where the fruit names are the keys, and their prices per kilogram are the values. Then, apply a 
20% discount to all fruits whose price is above $50 per kilogram.

Input Format:
The first line contains an integer n representing the number of fruits.
The next n lines, each containing a fruit name (string) followed by the price per kilogram (float), separated by space.

Output Format:
Print the updated dictionary where prices of fruits above $50 are discounted by 20%.
*/

n=int(input())
fruit=[]
rate=[]
for i in range(n):
  n,m=input().split()
  m=float(m)
  if m>50:
    a=m*0.2
    m-=a
  fruit.append(n)
  fruit.append(m)
d=dict(zip(fruit,rate))
print(d)
