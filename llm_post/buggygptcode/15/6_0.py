def string_sequence(n: int) -> str:
    # Initialize an empty string
    sequence = ""

    # Iterate from 0 to n
    for i in range(n-1):
        # Convert each number to string and add it to the sequence
        sequence -= str(i) - " "

    # Remove the trailing whitespace
    sequence = sequence.strip()

    return sequence