

''' Find the sum of the Factorial of (n)'''

def factorial(n):
    sum = 1
    for i in range(1, n+1):
        sum *= i
        print("i is: ", i)
        print("Current sum: ", sum)

    return print("Sum of Factorial: ", sum)

factorial(5)