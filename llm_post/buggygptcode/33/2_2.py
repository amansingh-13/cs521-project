def sort_third(l: list):
    # create a new empty list to store the sorted values
    l_sorted = []
    # iterate over the elements in the original list
    for i in range(len(l)):
        # check if the index is divisible by three
        if i % 3 != 0:
            # get the values at the corresponding indices in the original list
            values = [l[j] for j in range(i, min(i+3, len(l)))]
            # sort the values
            values.sort()
            # add the sorted values to the new list
            l_sorted.extend(values)
        else:
            # add the value from the original list to the new list
            l_sorted.append(l[i])
    # return the new list
    return l_sorted