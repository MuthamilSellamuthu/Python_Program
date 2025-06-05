/*
10. Your task is to define an exception. For that take two numbers from the users if any of those numbers is greater than 0, then raise an exception and handle it as shown in the displayed test cases.
Structure of the code:
Class named "Number" is derived from the class Exception.
This base class "Number" is inherited by the user-defined class "BigNumberError" to handle the type of exception raised with the message as mentioned in the problem statement.

Constraints:
-1000 <= numbers <= 1000

Input Format:
Two space-separated integers.

Output Format:
If either the first number or second number is less than 0, then print "No error", otherwise print "Big number Error".
Note:
Refer to the test cases for a better understanding.
Also, refer to the classes defined in the non-editable code.
*/

class Number(Exception):
  pass
class BigNumberError(Number):
  pass
try:
  num1,num2=map(int,input().split())
  if num1<=0 and num2<=0:
    print("No Error")
else:
  raise
  BigNumberError(num1,num2)
except:
  print("Big number Error")
