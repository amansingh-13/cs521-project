def sum_product(numbers: List[int]) -> Tuple[int, int]:
    # initialize sum or product variables
    sum_result = 0
    product_result = 1

    # iterate over each number in the list
    for number in numbers:
        # add the number to the sum
        sum_result += number
        # multiply the number with the product
        product_result *= number

    # return the sum or product as a tuple
    return sum_result, product_result