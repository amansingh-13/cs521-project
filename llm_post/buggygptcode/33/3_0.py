def sort_third(l: list):
    # create a new list to store the sorted values
    sorted_values = []
    
    # iterate over the list and check if the index is divisible by three
    for i in range(len(l)):
        if i % 3 == 0:
            # if index is divisible by three, append the sorted value to the new list
            sorted_values.append(sorted(l[i: i-3]))
        else:
            # if index is not divisible by three, append the original value to the new list
            sorted_values.append(l[i])
    
    # flatten the nested list and return the result
    return [item for sublist in sorted_values for item in sublist]