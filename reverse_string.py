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