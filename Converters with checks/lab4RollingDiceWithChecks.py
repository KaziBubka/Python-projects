import random

rollAgain = True

while rollAgain:
    # Asking the user for the number of faces of the dice (between 1 and 23 inclusive), and saving user input to a variable
    numberOfFaces = input(
        "Enter the number of faces of the dice between 1 and 23: ")

    while numberOfFaces.isdigit() != True or int(numberOfFaces) > 23:
        numberOfFaces = input(
            "Enter a positive integer between 1 and 23: ")
    pass

    # Converting user input to int
    numberOfFaces = int(numberOfFaces)

    # Generating a random value using randint function
    generatedValue = random.randint(1, numberOfFaces)

    # Printing the output
    print("The program generated a value of {0} for a dice of {1} faces.".format(
        generatedValue, numberOfFaces))

    rollAgain = input("Do you want to roll again? yes or no: ")

    if rollAgain == "no":
        rollAgain = False
        break

print("Thanks for rolling!")
