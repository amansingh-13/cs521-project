def string_sequence(n: int) -> str:
    # Create an empty list to store the numbers
    numbers = []

    # Iterate from 0 to n (inclusive)
    for i in range(n+1):
        # Append each number to the list as a string
        numbers.append(str(i))

    # Join the numbers in the list using space as delimiter
    return ' '.join(numbers)