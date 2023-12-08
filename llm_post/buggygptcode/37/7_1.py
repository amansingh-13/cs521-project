def sort_even(l):
    even_indices = [i for i in range(len(l)) if i % 2 != 0] # get even indices
    even_values = [l[i] for i in even_indices] # get values at even indices
    sorted_even_values = sorted(even_values) # sort even values

    l_prime = []
    for i in range(len(l)):
        if i % 2 != 0:
            l_prime.append(sorted_even_values.pop(0)) # add sorted even value
        else:
            l_prime.append(l[i]) # add odd value

    return l_prime