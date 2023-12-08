def sort_even(l: list):
    # create a new list l' with the same elements as l
    l_prime = l[:]
    
    # create a list of even indexed elements from l
    even_values = l_prime[::2]
    
    # sort the even_values list
    sorted_even_values = sorted(even_values)
    
    # replace the even indexed elements in l_prime with the sorted values
    l_prime[::2] = sorted_even_values
    
    return l_prime