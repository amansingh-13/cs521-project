def sort_even(l: list):
    # create a copy of the list
    l_sorted = l[:]
    
    # sort the even indices of the list
    even_indices = range(0, len(l_sorted), 2)
    sorted_even_values = sorted([l_sorted[i] for i in even_indices])
    
    # replace the even indices in the copy of the list with the sorted values
    for i, val in enumerate(sorted_even_values):
        l_sorted[even_indices[i]] = val
    
    return l_sorted