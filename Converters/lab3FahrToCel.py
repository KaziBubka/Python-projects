# Asking the user to input the temperature in Fahrenheit, and converting it to float
fahrenheit = float(input("Please enter the temperature in Farhenheit:"))

# Multiplying to get the temperature in Celcius
temperatureInCelcius = (fahrenheit - 32)/1.8

# rounding the output to 2 decimal places
temperatureInCelcius = round(temperatureInCelcius, 2)

# Converting the result to str for printing
temperatureInCelcius = str(temperatureInCelcius)

# Printing the result
print("The temperature in Celcius is " + temperatureInCelcius)
