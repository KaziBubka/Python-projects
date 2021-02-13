def instructions():
    print("Instructions: Enter a number to find its factorial")


instructions()


n = input("Enter a number: ") or 0


def factorialFunction():
    factorial = 1
    if int(n) >= 1:
        for i in range(1, int(n)+1):
            factorial = factorial * i

    print("Factorial of ", n, " is : ", factorial)


factorialFunction()

input("Press any key to exit")
