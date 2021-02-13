"""
Kazi Bubka - 041012034
Last Modified On- 24/09/2020
Input- Number of faces of the dice
Output- Generated value
"""

# importing the random library
import random

# Asking the user for the number of faces of the dice (maximum of 10), and saving user input to a variable
numberOfFaces = input(
    "Please enter the number of faces of your dice (Max 10)>> ")

# Converting user input into the correct data type (integer)
numberOfFaces = int(numberOfFaces)

if (numberOfFaces > 10):  # Checking for specified range of input
    print("Please enter a number between 0 and 10!")
elif (numberOfFaces < 1):  # Checking for positive integer
    print("The number you enter must be a positive integer!")
else:
    generatedValue = random.randint(
        1, numberOfFaces)  # Generating a random value using randint function

    print("The computer generated the value {0} on a dice with {1} faces.".format(
        generatedValue, numberOfFaces))  # Printing the output
