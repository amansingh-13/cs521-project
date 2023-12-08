def pairs_sum_to_zero(l):
    # Create a set to store unique elements in the list
    unique_elements = set(l)

    # Iterate through each element in the list
    for num in l:
        # Check if the negative of the current element exists in the set
        if -num in unique_elements:
            # If so, return True
            return True

    # If no pair is found, return False
    return False