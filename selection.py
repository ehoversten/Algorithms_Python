""" Selection Sort """


def selectionSort(arr):
    # Loop through array starting from the end
    for idx in range(len(arr)-1, 0, -1):
        maxIdx = 0

        # For every set of 0 to index+1
        for elem in range(1, idx+1):
            # Set maximum's location
            if arr[elem] > arr[maxIdx]:
                maxIdx = elem
        
        # SWAP indexes 
        temp = arr[idx]
        arr[idx] = arr[maxIdx]
        arr[maxIdx] = temp

    return arr


arr1 = [5, 3, 2, 1, 4]
print(arr1)
selectionSort(arr1)
print(arr1)
