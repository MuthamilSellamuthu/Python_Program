/*You are designing a class hierarchy to manage information about different vehicles. Follow the instructions below to implement the required functionality:

Create a base class named Vehicle with the following characteristics:
An attribute model that stores the model of the vehicle as a string.
An attribute year that stores the year of the vehicle as an integer.
A method inputDetails() that takes user input for the model and year of the vehicle.
A method displayDetails() that returns the model and year formatted as a string, with the model on the first line and the year on the second line.
Implement a child class named Car that inherits from the Vehicle class. The Car class should have the following characteristics:
An attribute isConvertible that stores whether the car is convertible or not as a boolean.
A method inputConvertible() that takes user input (true/false) for whether the car is convertible.
A method displayConvertible() that returns whether the car is convertible as a string.
A unique feature: In the Car class, implement a method named generateLicensePlate() that generates a license plate for the car using the first three characters of the model (converted to uppercase), followed by a hyphen, and the last two digits of the year. This method should return the generated license plate.

Input Format:
The first line of input is a string representing the model of the vehicle.
The second line of input is an integer representing the year of the vehicle.
The third line of input is a boolean (true/false) representing whether the car is convertible.

Output Format:
The first line is the string representing the model of the vehicle.
The second line is the integer representing the year of the vehicle.
The third line is the boolean representing whether the car is convertible.
The fourth line is the license plate generated based on the unique feature.

Note: Length of the name of the car model is always greater than 2
*/

class Vehicle:
  def inputDetails(self):
    self.model=input()
    self.year=input()
  def displayDetails(self):
    return f"{self.model}\n{self.year}"
class Car(Vehicle):
  def inputConvertible(self):
    self.isConvertible=input()=='true'
  def displayConvertible(self):
    return f"{str(self.isConvertible)}"
  def generateLicensePlate(self):
    return f"{self.model[0:3].upper()}-{self.year[-2:]}"
if __name__=="__main__":
  car=Car()
  car.inputDetails()
  car.inputConvertible()
  details=car.displayDetails()
  convertible_status=car.displayConvertible()
  license_plate=car.generateLicensePlate()
  print(details)
  print(convertible_status)
  print(license_plate)
