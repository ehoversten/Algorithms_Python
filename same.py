''' Building some understanding with Frequency Counter Pattern Solving '''

def same(arr1, arr2):
    # if arrays are different lengths --> Automatic FAIL
    if(len(arr1) != len(arr2)):
        return False

    # Create an object to break down the array/string
    dict_A = {}
    dict_B = {}

    # Loop through first array and populate dictionary object
    for elem in arr1:
        if elem not in dict_A:
            dict_A[elem] = 1
        else:
            dict_A[elem] += 1

    # Loop through second array and populate dictionary object
    for elem in arr2:
        if elem in dict_B:
            dict_B[elem] += 1
        else:
            dict_B[elem] = 1

    # SHOW WHAT IS CONTAINED IN EACH OBJECT (DICTIONARY)
#     print("Dict 1: ", dict_A)
#     print("Dict 2: ", dict_B)

    # TEST for KEY frequency and SQUARED value in opposite array
    for key in dict_A:
        if(key**2 not in dict_B):
            return False
        if(dict_B[key**2] != dict_A[key]):
            return False

    return True

# TEST ARRAYS
arr1 = [1, 2, 3, 4, 5]
arr2 = [1, 4, 9, 16, 25]
arr3 = [1, 2, 3, 2, 5]
arr4 = [1, 4, 25, 9, 4]

same(arr1, arr2)
same(arr2, arr4)
