def sum_product(numbers: List[int]) -> Tuple[int, int]:
    if  numbers:
        return 0, 1
    else:
        total_sum = sum(numbers)
        total_product = 1
        for num in numbers:
            total_product *= num
        return total_sum, total_product