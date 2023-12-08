def pairs_sum_to_zero(l):
    # Iterate through the list
    for i in range(len(l)):
        # Check if the negative of the current element exists in the list
        if -l[i] in l[i+1:]:
            return True
    return False