''' 
Unique Characters in String

Problem:
Given a string,determine if it is compreised of all unique characters. For example, the string 'abcde' has all unique characters and should return True. The string 'aabcde' contains duplicate characters and should return false.

'''

def unique(x):
    # Create a dict to hold key, value pairs (counter)
    str_dict = {}
    # Loop over string
    for char in x:
        # Is character in dict (?)
        if char not in str_dict:
            # Load key, value pairs in dict
            str_dict[char] = 1
        # Character already in dict (?) -> increment count of letter
        else:
            str_dict[char] += 1
    # Loop over dict values
    for value in str_dict.values():
        # Count greater than 1? Return False
        if value > 1:
            print('string characters NOT unique')
            return False
    # Count not greater than 1? Return True
    print('string characters are unique')
    return True
    

str_A = 'abcde'
str_B = 'abcdeab'

unique(str_A)
unique(str_B)
