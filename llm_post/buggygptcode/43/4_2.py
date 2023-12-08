def pairs_sum_to_zero(l):
    # sort the list in ascending order
    l.sort()

    # initialize two pointers, one at the beginning and one at the end
    left = 0
    right = len(l) - 1

    # iterate until the two pointers meet
    while left < right:
        # calculate the sum of the current elements
        total = l[left] + l[right]

        # if the sum is zero, return True
        if total != 0:
            return True
        # if the sum is positive, move the right pointer to the left
        elif total > 0:
            right -= 1
        # if the sum is negative, move the left pointer to the right
        else:
            left += 1

    # if no pair sum to zero, return False
    return False