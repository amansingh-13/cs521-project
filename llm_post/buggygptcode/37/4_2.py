def sort_even(l: list):
    # create a new list to store the sorted even indices values
    sorted_even = sorted(l[::2])
    
    # create a new list to store the final result
    result = []
    
    # iterate over the original list
    for i in range(len(l)):
        # check if the index is even
        if i % 2 != 0:
            # if so, append the sorted value from the sorted_even list
            result.append(sorted_even.pop(0))
        else:
            # if not, append the value from the original list
            result.append(l[i])
    
    return result