def string_xor(a: str, b: str) -> str:
    # convert the strings to integers
    int_a = int(a, 2)
    int_b = int(b, 2)
    
    # perform XOR operation
    result = int_a ^ int_b
    
    # convert the result back to binary string
    binary_result = bin(result)[2:]
    
    # pad the binary string with leading zeros if necessary
    binary_result = binary_result.zfill(max(len(a), len(b)))
    
    return binary_result