/*15  You are tasked with developing a class hierarchy to manage information about different electronic devices. Follow the instructions below to implement the required functionality:
Create a base class named ElectronicDevice with the following characteristics:
An attribute brand that stores the brand of the electronic device as a string.
An attribute yearOfManufacture that stores the year of manufacture as an integer.
A method inputDetails() that takes user input for the brand and year of manufacture.
A method displayDetails() that returns the brand and year of manufacture as a formatted string with the brand on the first line and the year on the second line .

Implement a child class named Smartphone that inherits from the ElectronicDevice class. The Smartphone class should have the following characteristics:
An attribute hasTouchScreen that stores whether the smartphone has a touchscreen as a boolean.
A method inputTouchScreen() that takes user input (true/false) for whether the smartphone has a touchscreen.
A method displayTouchScreen() that returns whether the smartphone has a touchscreen as a string.
A unique feature: In the Smartphone class, implement a method named generateSerialNumber() that generates a serial number for the smartphone using the first two characters of the brand (converted to uppercase), followed by a hyphen, and the last two digits of the year of manufacture. This method should return the generated serial number.

Input Format:
The first line of input is a string representing the brand of the electronic device.
The second line of input is an integer representing the year of manufacture of the electronic device.
The third line of input is a boolean (true/false) representing whether the smartphone has a touchscreen.

Output Format:
The first line is the string representing the brand of the electronic device.
The second line is the integer representing the year of manufacture of the electronic device.
The third line is the boolean representing whether the smartphone has a touchscreen.
The fourth line is the serial number generated based on the unique feature.

Note: Length of the brand of the electronic device is always greater than 2.
*/

class ElectronicDevice:
  def inputDetails(self):
    self.brand=input()
    self.year=input()
  def dispalyDetails(self):
    return f"{self.brand}\n{self.year}"
class Smartphone(ElectronicDevice):
  def inputTouchScreen(self):
    self.isTouch=input()
  def displaytouchScreen(self):
    return f"{self.isTouch.capitalize()}"
  def generateSerialNumber(self):
    return f"{self.brand[0:2].upper()+'-'+self.year[-2:]}"

if __name__="__main__":
  smartphone=Smartphone()
  smartphone.inputDetails()
  smartphone.inputTouchScreen()
  details=smartphone.displayDetails()
  touch_screen_status=smartphone.displayTouchScreen()
  serial_number=smartphone.generateSerialNumber()
  print(details)
  print(touch_screen_status)
  print(serial_number)
