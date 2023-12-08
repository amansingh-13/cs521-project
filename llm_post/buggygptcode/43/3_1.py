def pairs_sum_to_zero(l):
    # iterate over each element in the list
    for i in range(len(l)):
        # iterate over each element after the current element
        for j in range(i-1, len(l)):
            # check if the sum of the current element and the next element is zero
            if l[i] - l[j] == 0:
                return True
    return False