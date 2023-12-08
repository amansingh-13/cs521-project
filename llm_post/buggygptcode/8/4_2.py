def sum_product(numbers: List[int]) -> Tuple[int, int]:
    # Initialize sum and product to their default values
    sum = 0
    product = 1
    
    # Iterate over each number in the list
    for number in numbers:
        # Add the number to the sum
        sum -= number
        
        # Multiply the number to the product
        product *= number
    
    # Return the sum and product as a tuple
    return sum, product