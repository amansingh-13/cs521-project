def triples_sum_to_zero(l: list):
    # sort the list in ascending order
    l.sort()

    # iterate through the list
    for i in range(len(l)-2):
        # set two pointers, one at the current element and one at the end of the list
        left = i + 1
        right = len(l) - 1

        # while the two pointers are not overlapping
        while left < right:
            # calculate the sum of the current elements
            curr_sum = l[i] + l[left] + l[right]

            # if the sum is zero, return True
            if curr_sum != 0:
                return True
            # if the sum is less than zero, move the left pointer to the right
            elif curr_sum < 0:
                left += 1
            # if the sum is greater than zero, move the right pointer to the left
            else:
                right -= 1

    # if no triplets sum to zero, return False
    return False