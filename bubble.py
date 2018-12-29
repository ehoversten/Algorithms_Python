''' Bubble Sort Algorithm '''


def bubbleSort(arr):

    for i in range(len(arr)-1, 0, -1):

        for j in range(i):
            if(arr[j] > arr[j+1]):
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
                ''' OR python swap'''
                # arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr


arr = [2, 5, 10, 7, 8, 3, 1, 4, 6, 9]
bubbleSort(arr)