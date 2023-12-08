def string_xor(a: str, b: str) -> str:
    # Convert the input strings to integers using base 2
    a_int = int(a, 2)
    b_int = int(b, 2)
    
    # Perform XOR operation on the integers
    result = a_int ^ b_int
    
    # Convert the result back to a binary string
    result_str = bin(result)[2:]
    
    # Pad the binary string with leading zeros if necessary
    result_str = result_str.zfill(max(len(a), len(b)))
    
    return result_str