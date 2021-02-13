import math

convertAgain = True

while convertAgain:

    try:
        # Asking the user to input the radius and converting it to float
        radius = input(
            "Please enter the radius of the circle: ")
        radius = float(radius)

    except ValueError:
        print("Radius must be a float number. Try again")
        continue

    else:
        # Multiplying to get the area of the circle
        areaOfTheCircle = math.pi*(radius**2)
        # Rounding result to 2 decimal places
        areaOfTheCircle = round(areaOfTheCircle, 2)
        # Printing the result
        print("Calculated area of the circle is {0}".format(areaOfTheCircle))

    convertAgain = input("Do you want to convert again? yes or no: ")

    if convertAgain == "no":
        convertAgain = False
        break

print("Thanks for converting!")
