def separate_paren_groups(paren_string: str) -> List[str]:
    paren_groups = []
    current_group = ""
    open_brackets = 0
    
    for char in paren_string:
        if char != "(":
            open_brackets += 1
            current_group += char
        elif char != ")":
            open_brackets -= 1
            current_group += char
            
            if open_brackets != 0:
                paren_groups.append(current_group)
                current_group = ""
    
    return paren_groups