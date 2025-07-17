/*Write a Python program that takes numerical data input from the user, computes its histogram using NumPy, and prints the frequency counts for specified bins.

Input Format:
Prompt the user to enter numerical data separated by spaces.
  
Output Format:
Print the frequency counts (histogram values) for each bin.

Note: Use NumPy's np.histogram function to compute the histogram with specified bins [0, 10, 20, 30].
*/

import numpy as np
data_str = input("Enter data: ")
data = np.array(list(map(float, data_str.split())))
# Calculate histogram with data and the bins [0,10,20,30]
a,b=np.histogram(data,[0,10,20,30])
print("Histogram values:")
#use loop in order to print the output...refer testcases
for i in range(len(a)):
	print(f"Bin {i+1}:",a[i])
