convertAgain = True

while convertAgain:

    try:
        # Asking for multiple inputs from the user and converting inputs to float
        exchangeRate = input(
            "Please enter the exchange rate from USD to CAD: ")
        exchangeRate = float(exchangeRate)

        amountToBeConverted = input(
            "Please enter the amount of USD to be converted: ")
        amountToBeConverted = float(amountToBeConverted)

    except ValueError:
        print("Exchange rate and amount must be a float number")
        continue

    else:
        # Multiplying to get converted amount
        convertedAmount = exchangeRate*amountToBeConverted
        convertedAmount = round(convertedAmount, 2)
        # Printing the result
        print("Converted amount in CAD is {0}".format(convertedAmount))

    convertAgain = input("Do you want to convert again? yes or no: ")

    if convertAgain == "no":
        convertAgain = False
        break

print("Thanks for converting!")
