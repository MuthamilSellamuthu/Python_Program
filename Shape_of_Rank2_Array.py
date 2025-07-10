/*Write a Python program to find the shape of rank 2 array using numpy module

Input Format:
The input should be a single line, where:
Each row of numbers is separated by a semicolon (;).
Each number within a row is separated by a space.

Output Format:
The array is printed in matrix form.
The shape of the matrix (number of rows and columns) is also displayed.

Note : Refer to sample test cases for better understanding
*/

import numpy as np
n=input().split(';')
arr=np.array([],dtype=int)
m=[]
for i in n:
  m=list(map(int,i.split()))
  arr=np.append(arr,m)
arr=arr.reshape(len(n),len(m))
print("Array:")
print(arr)
print("Shape:",arr.shape)
