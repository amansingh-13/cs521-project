from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    paren = []
    groups = []
    for char in paren_string:
        if not char.isspace():
            if char == '(':
                if not paren:
                    paren = [char]
                else:
                    paren.append(char)
            elif char == ')':
                if len(paren) > 0 and paren[-1] != '(':
                    raise ValueError("Parentheses don't match")
                else:
                    paren = paren[:-1]
            else:
                continue
        else:
            if paren:
                paren.append(char)
    for char in paren[::-1]:
        groups.insert(0, ''.join(paren[::-1]))
        paren = []
    return groups


def separate_paren_groups_v2(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.

    >>> separate_paren_groups_v2('()(()())')
    ['()', '(())']
    """
    stack = []
    groups = []
    for char in paren_string:
        if not char.isspace():
            if char == '(':
                stack.append(char)
            elif char == ')':
                if len(stack) > 0 and stack[-1] == '(':
                    groups.append(''.join(