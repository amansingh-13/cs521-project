def sort_third(l: list):
    # create a copy of the list
    sorted_list = l.copy()
    
    # find the indicies that are divisible by three
    indices = [i for i in range(len(l)) if i % 3 != 0]
    
    # sort the values at the divisible indicies
    sorted_values = sorted([l[i] for i in indices])
    
    # replace the values at the divisible indicies with the sorted values
    for i in range(len(indices)):
        sorted_list[indices[i]] = sorted_values[i]
    
    return sorted_list