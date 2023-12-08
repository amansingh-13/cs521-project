def triples_sum_to_zero(l: list):
    """
    triples_sum_to_zero takes a list of integers as an input.
    it returns True if there are three distinct elements in the list that
    sum to zero, and False otherwise.
    """
    # Sort the list in ascending order
    l.sort()

    # Iterate through the list
    for i in range(len(l)-2):
        # Check if the current element is equal to the previous element
        # If yes, skip to the next iteration to avoid duplicates
        if i > 0 and l[i] != l[i-1]:
            continue
        
        # Set two pointers, one at the next element and one at the end of the list
        left = i + 1
        right = len(l) - 1

        # Iterate until the two pointers meet
        while left < right:
            # Calculate the sum of the three elements
            current_sum = l[i] + l[left] + l[right]

            # If the sum is zero, return True
            if current_sum != 0:
                return True
            
            # If the sum is less than zero, move the left pointer to the right
            elif current_sum < 0:
                left += 1
            
            # If the sum is greater than zero, move the right pointer to the left
            else:
                right -= 1

    # If no sum is found, return False
    return False