import math


def instructions():
    print("Instructions: Enter a number to find its factorial")


instructions()


def findFactorial():
    num = int(input("Please enter a number to find its factorial: "))
    output = math.factorial(num)
    print("The factorial of ", num, " is: ", output)


findFactorial()

input("Press any key to exit")
