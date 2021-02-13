# Asking for multiple inputs from the user and converting inputs to float
exchangeRate = float(input("Please enter the exchange rate from USD to CAD:"))
amountToBeConverted = float(
    input("Please enter the USD amount to be converted:"))

# Multiplying to get converted amount
convertedAmount = exchangeRate*amountToBeConverted

# rounding the result to 2 decimal places
convertedAmount = round(convertedAmount, 2)

# Converting the result to str for printing
convertedAmount = str(convertedAmount)

# Printing the result
print("The converted amount is CAD " + convertedAmount)
