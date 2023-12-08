def sort_even(l: list):
    # Create two separate lists for odd indices and even indices
    odd_indices = l[1::2]
    even_indices = l[::2]
    
    # Sort the even indices list
    sorted_even_indices = sorted(even_indices)
    
    # Combine the sorted even indices list with the odd indices list
    sorted_list = [sorted_even_indices[i//2] if i % 2 != 0 else odd_indices[i//2] for i in range(len(l))]
    
    return sorted_list