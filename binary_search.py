def binary_search(arr, element):
    ''' Search a sorted list for a given value '''
    # initalize a start and end index's
    start = arr[0]
    end = arr[len(arr)-1]
    
    found = False
    # count of iterations
    count = 1
    
    while start <= end and not found:
        midpoint = (start + end) // 2
        
        # Search matches element in array 
        if arr[midpoint] == element:
            found = True

        # Set new midpoints up or down depending on comparison
        else:
            # Set down
            if element < arr[midpoint]:
                count += 1
                end = midpoint - 1
            # Set up 
            else:
                count += 1
                start = midpoint + 1
        
    # print("Iterations: ", count)
    return print("Found: ", found)


# list must already be sorted!
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

binary_search(arr, 2.5)

#binary_search(arr, 10)
