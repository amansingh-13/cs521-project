def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    """
    # Initialize a set to keep track of seen elements
    seen = set()
    
    # Iterate through each element in the list
    for num in l:
        # Check if the negative of the current element is in the set
        if -num in seen:
            return True
        # Add the current element to the set
        seen.add(num)
    
    # If no pair sum to zero, return False
    return False

# Testing the function
print(pairs_sum_to_zero([1, 3, 5, 0])) # False
print(pairs_sum_to_zero([1, 3, -2, 1])) # False
print(pairs_sum_to_zero([1, 2, 3, 7])) # False
print(pairs_sum_to_zero([2, 4, -5, 3, 5, 7])) # True
print(pairs_sum_to_zero([1])) # False