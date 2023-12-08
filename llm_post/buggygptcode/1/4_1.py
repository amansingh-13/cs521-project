def separate_paren_groups(paren_string: str) -> List[str]:
    groups = []
    paren_count = 0
    current_group = ''
    
    for char in paren_string:
        if char == '(':
            paren_count += 1
            current_group += char
        elif char == ')':
            paren_count -= 1
            current_group += char
            
            if paren_count == 0:
                groups.append(current_group)
                current_group = ''
        elif char == ' ':
            current_group += char
    
    return groups