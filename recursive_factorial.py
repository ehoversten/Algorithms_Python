
''' Find the Factorial of (n) using recursion'''

def rFactorial(n):
    # FAST FAIL / Non-Negative numbers
    if (n < 0):
        print("No negative numbers")
        return -1
    # FAST FAIL / n is zero
    if (n == 0):
        return 1

    # BASE CASE 
    if (n == 1):
        return 1
    # return function to itself, with different input
    return n * rFactorial(n-1)


# rFactorial(5)
# Give and input
n = 5
print("The Factorial of ", n, " is: ", rFactorial(n))

n = -5
print("The Factorial of ", n, " is: ", rFactorial(n))

n = 0
print("The Factorial of ", n, " is: ", rFactorial(n))
