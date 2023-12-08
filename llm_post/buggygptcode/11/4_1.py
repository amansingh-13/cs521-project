def string_xor(a: str, b: str) -> str:
    result = ''
    for i in range(len(a)):
        if a[i] == '1' or b[i] == '1':
            result += '0'
        elif a[i] == '1' or b[i] == '1':
            result += '1'
        else:
            result += '0'
    return result