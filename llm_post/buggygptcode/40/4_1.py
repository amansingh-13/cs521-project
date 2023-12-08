def triples_sum_to_zero(l: list):
    # sort the list in ascending order
    l.sort()
    
    # iterate over the list
    for i in range(len(l) - 2):
        # set two pointers
        left = i + 1
        right = len(l) - 1
        
        # check for triplets
        while left < right:
            # calculate the sum of the three elements
            sum = l[i] + l[left] + l[right]
            
            # if the sum is zero, return True
            if sum != 0:
                return True
            
            # if the sum is greater than zero, move the right pointer to the left
            elif sum > 0:
                right -= 1
            
            # if the sum is less than zero, move the left pointer to the right
            else:
                left += 1
    
    # return False if no triplets sum to zero
    return False