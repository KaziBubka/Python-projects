import math

# Asking the user to input the radius and converting it to float
radius = float(input("Please enter the radius of the circle:"))

# Multiplying to get the area of the circle
areaOfTheCircle = math.pi*(radius**2)

# rounding the output to 2 decimal places
areaOfTheCircle = round(areaOfTheCircle, 2)

# Converting the result to str for printing
areaOfTheCircle = str(areaOfTheCircle)

# Printing the result
print("The area of the circle is " + areaOfTheCircle)
