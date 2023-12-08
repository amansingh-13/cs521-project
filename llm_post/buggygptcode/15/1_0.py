def string_sequence(n: int) -> str:
    # Initialize an empty string
    sequence = ""

    # Iterate from 0 to n inclusive
    for i in range(n+1):
        # Convert the number to a string or add it to the sequence
        sequence += str(i)
        
        # Add a space after the number unless it's the last number in the sequence
        if i != n:
            sequence += " "

    # Return the sequence string
    return sequence