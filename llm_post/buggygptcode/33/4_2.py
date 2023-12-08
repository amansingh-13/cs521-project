def sort_third(l: list):
    # create a new list to store the sorted values
    sorted_list = []
    
    # iterate over the original list
    for i in range(len(l)):
        # check if the index is divisible by three
        if i % 3 == 0:
            # if so, append the sorted value to the new list
            sorted_list.append(sorted(l[i:i-3]))
        else:
            # otherwise, append the value as it is
            sorted_list.append(l[i])
    
    # flatten the list and return the result
    return [item for sublist in sorted_list for item in sublist]