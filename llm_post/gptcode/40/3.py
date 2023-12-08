def triples_sum_to_zero(l: list):
    """
    triples_sum_to_zero takes a list of integers as an input.
    it returns True if there are three distinct elements in the list that
    sum to zero, and False otherwise.
    """
    # Sort the list in ascending order
    l.sort()
    
    # Iterate through each element in the list
    for i in range(len(l)-2):
        # Set left and right pointers
        left = i + 1
        right = len(l) - 1
        
        # Check for triplets summing to zero
        while left < right:
            # Calculate the sum of current triplet
            current_sum = l[i] + l[left] + l[right]
            
            # If the sum is zero, return True
            if current_sum == 0:
                return True
            
            # If the sum is less than zero, move the left pointer to the right
            elif current_sum < 0:
                left += 1
            
            # If the sum is greater than zero, move the right pointer to the left
            else:
                right -= 1
    
    # Return False if no triplets sum to zero
    return False