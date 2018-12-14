''' Given a string, return a reverse of the string. '''

def reverseString(some_str):
    # create a list to hold a reversed string
    rvs_arr = []

    # create an decrementer 
    count = len(some_str)
    
    # loop through given string in reverse order
    while count != 0:
        # append characters to new array (starting from the end of given string)
        rvs_arr.append(some_str[count-1])
        # decrement count
        count = count - 1
        
    # convert array to string
    rvs_str = "".join(rvs_arr)
    
    # return new string list  
    return rvs_str


x = [1, 2, 3, 4, 5]


def rev(arr):
    rvsArr = arr[::-1]
    print(rvsArr)
    return rvsArr

def reverse_string3(s):
    """Return a reversed copy of `s`"""

    # strings in python are immutable, so we need to create a list to manipulate the string
    chars = list(s)
    # Loop through the first half of the string
    for i in range(len(s) // 2):
        print("i : ", i)
        tmp = chars[i]
        print("tmp: ", tmp)
        chars[i] = chars[len(s) - i - 1]
        print("char[i]: ", chars[i])
        chars[len(s) - i - 1] = tmp
        print("Temp now: ", tmp)
    return ''.join(chars)


reverse_string3("cats")
