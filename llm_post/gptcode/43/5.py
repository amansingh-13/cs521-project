def pairs_sum_to_zero(l):
    # check if the length of the list is less than 2, if so, return False
    if len(l) < 2:
        return False
    
    # create a set to store the complement of each element in the list
    complements = set()
    
    # iterate through each element in the list
    for num in l:
        # if the complement of the current element exists in the set, return True
        if -num in complements:
            return True
        # otherwise, add the complement of the current element to the set
        complements.add(num)
    
    # if no pairs sum to zero, return False
    return False