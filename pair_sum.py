''' 
Problem:
Given an integer array, output all the unique pairs that sum up to a specific value k.

So the input:

pair_sum([1,3,2,2],4)

would return 2 pairs:

 (1,3)
 (2,2)

'''

def pair_sum(arr,k):
    
    if len(arr)<2:
        return
    
    # Initalize Sets for tracking
    seen = set()
    output = set()
    
    # Loop through each number in array
    for num in arr:
        print("num: ", num)
        # Set target difference
        target = k-num
        print("target: ", target)
        # Add it to set if target hasn't been seen
        if target not in seen:
            print("Target not in set, adding num ->", num)
            seen.add(num)
            print("Seen Set: ", seen)
        else:
            print("Target in Seen {SET} !")
            # Add a tuple with the corresponding pair
            output.add( (min(num,target),  max(num,target)) )
            print("Adding to Output {SET} ->", (min(num,target),  max(num,target)))
            print("Output -> ", output)
    

    print('\n'.join(map(str,list(output))))
    return len(output)


pair_sum([1, 3, 2, 2], 4)
pair_sum([1, 3, 2, 2, 4, 0], 4)
