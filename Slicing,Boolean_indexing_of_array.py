/*Write a python program to demonstrate basic slicing, integer and Boolean indexing of array using NumPy operations. Your program should handle basic slicing, integer indexing, and boolean indexing operations on the array.

Input & Output Format:
First line: Two integers specifying number of rows (rows) and columns (cols) of the array (space separated).
Then, display the NumPy array after constructing it from the provided input elements row wise space separated.
Next line: Two integers (start and end) specifying the range of rows to slice from the array (space separated).
Then, display the sliced portion of the array based on the start and end indices. If the indices are invalid, output "Invalid". (The start index should be non-negative and less than the number of rows, and end index (end) should be within the range of rows to consider it as invalid).
Next line: An integer (index) specifying the position to access an element using integer indexing.
Display the element in the array at the specified index. If the index is invalid, output "Invalid"(index should be a non-negative integer less than the number of rows in the array).
Next line: A string of space-separated integers (0 or 1) representing boolean indices for selecting rows from the array.
Display the boolean index array used for selection followed by elements from the array that correspond to True values in the boolean index array.
*/

import numpy as np
a,b=map(int,input().split())
arr=np.array([],dtype=int)
for i in range(a):
  n=list(map(int,input().split()))
  arr=np.append(arr,n)
arr=arr.reshape(a,b)
print(arr)
n,m=map(int,input().split())
if(-1<n<m and n<b and m<b):
  print(arr[n:m])
else:
  print("Invalid")
n=int(input())
if(-1<n<a):
  print(arr[n])
else:
  print("Invalid")
a=list(map(int,input().split()))
if(len(arr)==0):
  print("Invalid")
else:
  m=np.array([],dtype=bool)
  for i in a:
    m=np.append(m,i==1)
  print(m)
  n=0
  k=np.array([],dtype=int)
  for i in range(len(a)):
    if(a[i]==1):
      k=np.append(k,arr[i])
      n+=1
    k=k.reshape(n,b)
    print(k)
