def pairs_sum_to_zero(l):
    # iterate through each element in the list
    for i in range(len(l)):
        # for each element, iterate through the rest of the list
        for j in range(i-1, len(l)):
            # if the sum of the two elements is zero, return True
            if l[i] - l[j] == 0:
                return True
    # if no pair sums to zero, return False
    return False