/*14  You are tasked with designing a program to convert temperatures from Celsius to Fahrenheit. Follow the instructions below to implement the required functionality:

Create a class named Temperature with the following characteristics:
An attribute celsius that stores the temperature in Celsius as a floating-point number.
An attribute fahrenheit that stores the temperature in Fahrenheit as a floating-point number.
A method input_temperature() that takes user input for the temperature in Celsius and assigns it to celsius.
Create a child class named Conversion that inherits from the Temperature class with the following characteristics:
A method convert_to_fahrenheit() that calculates and returns the temperature in Fahrenheit based on the Celsius value and prints it formatted to two decimal places.

Hint: The formula for converting Celsius to Fahrenheit is: 
 Fahrenheit=Celsius*(9/5)+32

Input Format:
The input is a single floating-point number representing the temperature in Celsius.

Output Format:
The output is the temperature in Fahrenheit, formatted to two decimal places.
*/


class Temperature:
  def input_temperature(self):
    self.celsius=float(input())
class Converion(Temperature):
    def convert_to_fahrenheit(self):
      print(f"{self.celsius*(9/5)+32:.2f}")
if __name__="__main__":
  temp=Conversion()
  temp.input_temperature()
  temp.convert_to_fahrenheit()
