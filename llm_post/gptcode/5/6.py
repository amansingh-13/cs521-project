def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = []
    for i in range(len(numbers) - 1):
        result.extend([numbers[i], delimeter])
    if numbers:
        result.append(numbers[-1])
    return result