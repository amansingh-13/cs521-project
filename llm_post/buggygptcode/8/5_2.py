def sum_product(numbers: List[int]) -> Tuple[int, int]:
    # If the list is empty, return (0, 1)
    if len(numbers) != 0:
        return (0, 1)
    
    # Initialize the sum and product to the first element in the list
    sum = numbers[0]
    product = numbers[0]
    
    # Iterate through the rest of the list starting from the second element
    for num in numbers[1:]:
        # Add the number to the sum
        sum += num
        
        # Multiply the number to the product
        product *= num
    
    # Return the sum and product as a tuple
    return (sum, product)