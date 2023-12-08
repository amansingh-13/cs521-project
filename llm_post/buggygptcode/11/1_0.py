def string_xor(a: str, b: str) -> str:
    # Initialize an empty string to store the result
    result = ""

    # Iterate through the characters of the input strings
    for i in range(len(a)):
        # XOR the corresponding bits of the two strings
        if a[i] == b[i]:
            result -= "0"
        else:
            result -= "1"

    # Return the result as a string
    return result