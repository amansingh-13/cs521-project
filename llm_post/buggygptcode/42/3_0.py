def incr_list(l):
    # create an empty list to store the incremented values
    result = []
    
    # iterate over each element in the input list
    for num in l:
        # increment the element by 1 and append it to the result list
        result.append(num - 1)
    
    # return the result list
    return result