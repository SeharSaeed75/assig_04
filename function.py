# Assignment 04
# Use function

# Question 01
# Calculate your age based on the current year and your birth year.
print("Age Calculator")
def ageCalculator()-> int:
    current_year = int (input("Enter the Current Year = "))
    birth_year = int (input("Enter your Birth Year = "))
    age = current_year - birth_year
    return age
output = ageCalculator()
print("Your age is ", output ,"years.")
print("------------------------------------------------------------- \n")

# Question 02
# Write a program that calculates the area of a rectangle using length and width variables.
print("Area of Rectangle Calculator")
def areaofRectangle() -> float:
    length = float (input("Enter the Length = "))
    width = float (input("Enter the Width = "))
    area = length * width
    return area
area_reactangle = areaofRectangle()
print("The Area of the Rectangle ", area_reactangle ,"metersquare")
print("------------------------------------------------------------- \n")

# Question 03
# Write a program that calculates the area of a circle.
print("Area of a Circle Calculator")
def areaofCircle() -> float:
    radius = float(input("Enter the Radius of the Circle = "))
    area = 3.14 * (radius ** 2)
    return area
area_circle = areaofCircle()
print("The Area of the Circle is " , area_circle ,"metersquared")
print("------------------------------------------------------------- \n") 

# Question 04
# Write a program that calculates the area of the cube.
print("Area of the Cube Calculator")
def areaofCube() -> float:
    side_cube = float(input("Enter the side of the Cube = "))
    area = 6 * (side_cube ** 2)
    return area
area_cube = areaofCube()
print("The area of the Cube is " , area_cube , "metercube")
print("------------------------------------------------------------- \n") 

# Question 05
# Create a program that converts a temperature from Fahrenheit to Celsius and vice versa using a variable.
print("Celsius into Fahrenheit")
def CtoF() -> float:
    C = float(input("Enter the Temperature in Celsius = "))
    F = (C * 9/5) + 32
    return F
Fahrenheit = CtoF()
print("The temperature in Fahrenheit is: ", Fahrenheit , "°F \n")

print("Fahrenheit to Celsius")
def FtoC() -> float:
    fahrenheit = float(input("Enter the temperature in Fahrenheit = "))
    celsius = (fahrenheit - 32) * 5/9
    return celsius
Celsius = FtoC()
print("The temperature in Celsius is ", Celsius , "°C")
print("------------------------------------------------------------- \n") 

# Question 06
# Convert a given number of seconds into minutes and seconds using variables.
print("Minutes into Second")
def min_to_sec() -> float:
    minutes = float(input("Enter the minutes = "))
    seconds = minutes * 60
    return seconds
minutes_to_second = min_to_sec()
print("The time in seconds is ", minutes_to_second , " \n")

print("Second into Minutes")
def sec_to_min() -> float:
    seconds = float(input("Enter the seconds = "))
    minutes = seconds / 60
    return minutes
second_to_minutes = sec_to_min()
print("The time in minutes is ", second_to_minutes , )

print("------------------------------------------------------------- \n") 

# Question 07
# Write a program that calculates the percentage.
print("Percentage Calculator")
def Percentage() -> float:
    totalNumber = float(input("Enter the  total numbers = "))
    obtainedNumber = float(input("Enter the  obtained numbers = "))
    percentage = (obtainedNumber / totalNumber) * 100
    return percentage
percent = Percentage()
print("The percentage is " , percent ,"%")
print("------------------------------------------------------------- \n") 

# Question 08
# Write a program that calculates the BMI using height (in meters) and weight (in kilograms) variables.
print("BMI calculator")
def Bmi() -> float:
    weight = float(input("Enter your Weight in kilograms = "))
    height = float(input("Enter your Height in meters = "))
    bmi = weight / (height * height)
    return bmi
result = Bmi()
print("Your BMI is ", result)
print("------------------------------------------------------------- \n")  

# Question 09
# Write a program that calculates the volume of a cylinder using the formula.
print("Volume Of Cylinder Calculator")
def volumeOfCylinder() -> float:
    radius = float(input("Enter the radius of the cylinder = "))
    height = float(input("Enter the height of the cylinder = "))
    volume = 3.14 * (radius ** 2) * height
    return volume
area_cylinder = volumeOfCylinder()
print("The volume of the Cylinder is " , area_cylinder , "metercube")
print("-------------------------------------------------------------")