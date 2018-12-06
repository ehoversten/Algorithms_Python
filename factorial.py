

''' Find the Factorial of (n)'''

def factorial(n):
    # Initalize variable to hold product of n
    total = 1

    for i in range(1, n+1):
        total *= i
        # print("i is: ", i)
        # print("Current total: ", total)

    return print("Total of Factorial: ", total)

factorial(5)
