def sort_third(l: list):
    # create a new list to store the sorted values
    sorted_values = []
    
    # iterate over the original list
    for i in range(len(l)):
        # check if the index is divisible by three
        if i % 3 != 0:
            # if divisible by three, add the sorted value to the new list
            sorted_values.append(sorted(l[i:i+3]))
        else:
            # if not divisible by three, add the value as it is to the new list
            sorted_values.append(l[i])
    
    # flatten the sorted_values list and return it
    return [val for sublist in sorted_values for val in sublist]