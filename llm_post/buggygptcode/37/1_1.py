def sort_even(l: list):
    # create a copy of the input list
    l_sorted = l[:]
    
    # iterate over even indices of the list
    for i in range(0, len(l_sorted), 2):
        # get the sublist of even indices and sort it
        sublist = l_sorted[i::2]
        sublist.sort()
        
        # replace the even indices in the copy list with the sorted values
        l_sorted[i::2] = sublist
    
    return l_sorted