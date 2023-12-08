def pairs_sum_to_zero(l):
    # check if the list has at least 2 elements
    if len(l) < 2:
        return False
    
    # create a set to keep track of the complements
    complements = set()
    
    # iterate over the list
    for num in l:
        # check if the complement of num is in the set
        if -num in complements:
            return True
        # add the num to the set
        complements.add(num)
    
    # if no pair sum to zero, return False
    return False