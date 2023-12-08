def separate_paren_groups(paren_string: str) -> List[str]:
    groups = []
    stack = []
    start_index = 0
    for i, char in enumerate(paren_string):
        if char == '(':
            stack.append(char)
        elif char == ')':
            stack.pop()
            if len(stack) == 0:
                groups.append(paren_string[start_index:i+1])
                start_index = i+1
    return groups