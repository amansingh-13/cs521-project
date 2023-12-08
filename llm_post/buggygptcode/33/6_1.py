def sort_third(l: list):
    # Create a new list to store the sorted values
    sorted_list = []

    # Iterate over the indices of the list
    for i in range(len(l)):
        # Check if the index is divisible by three
        if i % 3 == 0:
            # If it is divisible by three, add the sorted value to the new list
            sorted_list.append(sorted(l[i:i-3]))
        else:
            # If it is not divisible by three, add the value as it is to the new list
            sorted_list.append(l[i])

    # Return the new sorted list
    return sorted_list