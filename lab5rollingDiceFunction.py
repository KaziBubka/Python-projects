import random


def instructions():
    print("Instructions: Choose an integer value to get an output")


instructions()


def rollingDice():
    numberOfFaces = int(
        input("Please enter the number of faces of the dice: "))
    generatedValue = random.randint(1, numberOfFaces)
    print("The program generated a value of {0} for a dice of {1} faces.".format(
        generatedValue, numberOfFaces))


rollingDice()

input("Press any key to exit")
