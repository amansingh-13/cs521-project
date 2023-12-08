def string_xor(a: str, b: str) -> str:
    # Convert the strings to integers using base 2
    int_a = int(a, 2)
    int_b = int(b, 2)
    
    # Perform XOR operation on the integers
    result = int_a ^ int_b
    
    # Convert the result back to a binary string
    binary_result = bin(result)
    
    # Remove the '0b' prefix from the binary string
    binary_result = binary_result[2:]
    
    # Pad the binary string with leading zeros if needed
    binary_result = binary_result.zfill(len(a))
    
    return binary_result