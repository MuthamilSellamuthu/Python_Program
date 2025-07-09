/*Write a Python program to create a NumPy array based on user input and display the following:
The created NumPy array.
The number of dimensions of the array using .ndim.
The shape of the array using .shape.
The total number of elements in the array using .size.
Assume all input elements are valid integers.

Input Format:
The first line contains two space-separated integers, r and c, representing the number of rows and the number of columns.
The next r lines contain c  space-separated integers representing the elements of the array, entered row by row.

Output Format:
The created NumPy array (printed as a 2D array).
An integer representing the number of dimensions of the array.
A tuple representing the shape of the array.
An integer representing the total number of elements in the array.

Note: Use reshape() function to reshape the input array with the specified number of rows and columns.
*/

import numpy as np
a,b=map(int,input().split())
arr=np.array([],dtype=int)
for i in range(a):
  n=list(map(int,input().split()))
  arr=np.append(arr,n)
arr=arr.reshape(a,b)
print(arr)
print(arr.ndim)
print(arr.shape)
print(arr.size)
