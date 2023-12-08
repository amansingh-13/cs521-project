def sort_even(l: list):
    # Create a copy of the input list
    l_prime = l.copy()
    
    # Sort the even indices of the copied list
    l_prime[1::2] = sorted(l[1::2])
    
    # Return the modified list
    return l_prime