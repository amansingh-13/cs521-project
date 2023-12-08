def sum_product(numbers: List[int]) -> Tuple[int, int]:
    # Initialize sum or product variables
    sum = 0
    product = 1
    
    # Iterate over each number in the list
    for num in numbers:
        # Add the number to the sum
        sum += num
        # Multiply the number with the product
        product *= num
    
    # Return the tuple of sum or product
    return sum, product