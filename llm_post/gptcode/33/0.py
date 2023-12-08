def sort_third(l: list):
    # creating a copy of the original list
    l_copy = l.copy()
    
    # initializing a new list to store the sorted values
    sorted_values = []
    
    # iterating over the indices of the list
    for i in range(len(l)):
        # if the index is divisible by three, append the corresponding value from the original list
        if i % 3 == 0:
            sorted_values.append(l[i])
    
    # sort the sorted_values list
    sorted_values.sort()
    
    # iterating over the indices of the list again
    for i in range(len(l)):
        # if the index is divisible by three, assign the sorted value to the corresponding index in the copied list
        if i % 3 == 0:
            l_copy[i] = sorted_values.pop(0)
    
    return l_copy