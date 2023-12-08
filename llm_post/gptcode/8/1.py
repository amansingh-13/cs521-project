def sum_product(numbers: List[int]) -> Tuple[int, int]:
    # Initialize the sum and product variables to their respective identities
    sum_result = 0
    product_result = 1

    # Iterate through each number in the list
    for number in numbers:
        # Add the number to the sum
        sum_result += number
        # Multiply the number to the product
        product_result *= number

    # Return the sum and product as a tuple
    return sum_result, product_result