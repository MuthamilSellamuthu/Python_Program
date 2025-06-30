/*You are tasked with designing a class hierarchy to perform calculations on numbers. The first task is to calculate the sum of the digits of a number. Then, we need to check if the sum of the digits is a perfect square.

Create a base class named NumberCalc with the following characteristics:
An attribute number that stores an integer.
A method inputNumber() that takes user input for the number attribute.
A method calculateSumOfDigits() that calculates and returns the sum of the digits of the entered number.
Implement a child class named PerfectSquareCheck that inherits from the NumberCalc class. The PerfectSquareCheck class should have the following characteristics:
A method isPerfectSquare() that checks whether the sum of the digits is a perfect square and returns a boolean value.

Input Format:
A single integer representing the number.

Output Format:
The sum of the digits of the entered number.
A boolean value(True/False) indicating whether the sum is a perfect square, each printed on a new line.

Hint: To check if a number is a perfect square, you can use the math module's sqrt() function. If the square of the square root equals the number, then it is a perfect square.
*/

import math
class NumberCalc:
  def __init__(self):
    self.number=0
  def inputNumber(self):
    self.number=int(input())
  def calculateSumofDigits(self):
    return sum(int(i) for i in str(Self.number))
class PerfectSquareCheck(NumberCalc):
  def isPerfectSquare(self):
    s_digits=self.calculateSumOfDigits()
    sv=int(math.sqrt(s_digits))
    return sv*sv==s_digits
calc=PerfectSquareCheck()
calc.inputNumber()
print(calc.calculateSumOfDigits())
print(calc.isPerfectSquare())

