
def linearSearch(arr, val):
    # loop through each element in given list/array
    for element in arr:
        # found value in list
        if(element == val):
            print("Found at idx: ", arr.index(element))
            return arr.index(element)
    # value not found in list
    print("Not Found in list")
    return -1


arr1 = [91, 94, 76, 65, 78, 89, 100]
linearSearch(arr1, 78)
linearSearch(arr1, 54)
