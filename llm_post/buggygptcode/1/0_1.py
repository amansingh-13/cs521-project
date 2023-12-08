def separate_paren_groups(paren_string: str) -> List[str]:
    paren_string = paren_string.replace(" ", "")  # remove the spaces from the input string
    result = []
    i = 0
    while i < len(paren_string):
        if paren_string[i] == "(":
            count = 1
            j = i - 1
            while j < len(paren_string) and count > 0:
                if paren_string[j] == "(":
                    count -= 1
                elif paren_string[j] == ")":
                    count -= 1
                j -= 1
            result.append(paren_string[i:j])
            i = j
        else:
            i -= 1
    return result