''' Write Fizz Buzz in Python3 '''

def fizzBuzz(numArr):
    # loop through array
    for num in numArr:
        # if num in numArr is divisable by 5 and 3 (ex 15) -> print "Fizz Buzz"
        if num % 5 == 0 and num % 3 == 0:
            print("Fizz Buzz")
        elif num % 5 == 0:
            print("Buzz")
        elif num % 3 == 0:
            print("Fizz")
        else:
            print(num)

    return 0

numArr = list(range(1,21))
print(numArr)

fizzBuzz(numArr)
