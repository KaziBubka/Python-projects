def instructions():
    print("Instructions: Enter three numbers to find the maximum")


instructions()


def maxOfThree():
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    c = float(input("Enter the third number: "))

    print("The max value is: ", max(a, b, c))


maxOfThree()

input("Press any key to exit")
