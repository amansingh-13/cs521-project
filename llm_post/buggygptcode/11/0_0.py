def string_xor(a: str, b: str) -> str:
    # Convert the strings to integers
    a_int = int(a, 2)
    b_int = int(b, 2)

    # Perform XOR operation
    result_int = a_int ^ b_int

    # Convert the result back to binary string
    result_str = bin(result_int)[2:]

    # Pad the result string with leading zeros if necessary
    return result_str.zfill(max(len(a), len(b)))