def sum_product(numbers: List[int]) -> Tuple[int, int]:
    # initialize sum and product variables
    sum_result = 0
    product_result = 1
    
    # iterate over the numbers in the list
    for num in numbers:
        # add the number to the sum
        sum_result += num
        # multiply the number with the product
        product_result *= num
    
    # return the sum and product as a tuple
    return (sum_result, product_result)