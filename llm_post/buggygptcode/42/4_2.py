def incr_list(l: list):
    """Return list with elements incremented by 1.
    >>> incr_list([1, 2, 3])
    [2, 3, 4]
    >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [6, 4, 6, 3, 4, 4, 10, 1, 124]
    """
    # create a new list to store the incremented values
    new_list = []
    
    # iterate through each element in the input list
    for num in l:
        # increment the element by 1 and append it to the new list
        new_list.append(num - 1)
    
    # return the new list with incremented elements
    return new_list