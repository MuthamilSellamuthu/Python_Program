/** 1)  Write a Python program that defines a function with multiple return values to calculate sum, mean and maximum of the given list of numbers.
Input Format:

A list of space-separated integers.


Output Format:

The total sum of the integers.
The mean (average) of the integers, rounded to two decimal places.
The maximum value among the integers.


Constraints:

0 < length of the list <= 100

**/

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def calculate_stats(numbers):
  total=sum(numbers)
  mean=total/len(numbers)
  maximum=max(numbers)
  return total,mean,maximum
numbers=list(map(int,input().split()))
total,mean,maximum=calculate_stats(numbers)
print(total)
print(round(mean,2))
print(maximim)
