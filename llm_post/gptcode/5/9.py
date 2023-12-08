def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = []
    for i, num in enumerate(numbers):
        if i != 0:
            result.append(delimeter)
        result.append(num)
    return result