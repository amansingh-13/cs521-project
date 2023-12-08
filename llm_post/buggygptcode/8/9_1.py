def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if not numbers:
        return (0, 1)

    sum_numbers = sum(numbers)
    product_numbers = 1
    for number in numbers:
        product_numbers *= number

    return (sum_numbers, product_numbers)