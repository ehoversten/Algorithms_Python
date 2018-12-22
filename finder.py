'''
Find missing element:

Given a sorted array, a second array is formed by shuffeling the elements and deleting one element. Given two arrays find the missing element

'''

import collections

def finder(arr1, arr2):

    # Using default dict to avoid key errors
    counter = collections.defaultdict(int)

    # Add a count for every instance in Array 1
    for num in arr2:
        counter[num] += 1

    # Check if num not in dictionary
    for num in arr1:
        if counter[num] == 0:
            print(num, "is missing")
            return num

        # Otherwise, subtract a count
        else:
            counter[num] -= 1
    

# def finder(arr1, arr2):
#     count_1 = {}
#     count_2 = {}

#     for elem in arr1:
#         if elem not in count_1:
#             count_1[elem] = 1
#         else:
#             count_1[elem] += 1
    
#     print("Dict1: " , count_1)

#     for elem in arr2:
#         if elem not in count_2:
#             count_2[elem] = 1
#         else:
#             count_2[elem] += 1

#     print("Dict2: ", count_2)


    # for num in arr2:
    #     if num not in count_1:
    #         count_1[num] = 1
    #     else:
    #         count_1[num] += 1

    ### THROWS ERROR ??? Not sure yet why this throws a KeyError
    # for num in arr1:
    #     if(count_1[num]==0):
    #         print(num, "is missing")
    #         return num
    #     else: 
    #         count_1[num] -= 1


#     return ("Error")

arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# arr1 = range(1, 6)
# randomize array
arr2 = [2, 5, 7, 3, 5, 1, 10, 8, 9, 4] # missing 6
# arr2 = [2, 4, 3, 5] # missing 3

finder(arr1, arr2)
