convertAgain = True

while convertAgain:

    try:
        # Asking the user to input the temperature in Fahrenheit, and converting it to float
        fahrenheit = input(
            "Please enter the temperature in Farhenheit: ")
        fahrenheit = float(fahrenheit)

    except ValueError:
        print("Temperature must be a float number. Please try again")
        continue

    else:
        # Multiplying to get the temperature in Celcius
        temperatureInCelcius = (fahrenheit - 32)/1.8
        temperatureInCelcius = round(temperatureInCelcius, 2)
        # Printing the result
        print("Temperature in Celcius is {0}".format(temperatureInCelcius))

    convertAgain = input("Do you want to convert again? yes or no: ")

    if convertAgain == "no":
        convertAgain = False
        break

print("Thanks for converting!")
