from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    # split on parentheses
    paren_string = paren_string.replace(' ', '')
    groups = []
    group = ""

    for char in paren_string:
        if char == "(":
            group += char
        elif char == ")":
            group += char
            groups.append(group)
            group = ""
        else:
            group += char
    return groups


def is_balanced(paren_string: str) -> bool:
    """ Return True if the parens in this string are balanced.
    >>> is_balanced('((()())(()))')
    True
    >>> is_balanced('((()))((()())(()))')
    False
    """
    # TODO: Fill this in.
    return True


def balance(paren_string):
    """ Return a string where all the un-paired parens have been paired off. 
    Assume that if there are no unmatched parens, then the string is already balanced.
    
    Assume we can add an "X" character to each side of every pair. Also, assume we want to do this using only one X for each pair.

    If you start with a single opening paren and make a matching closing paren after it, you would end up with two pairs. 
    
    >>> balance('((()))')
    '(X()())'
    """
    # Fill this in.


def remove_outermost_parens(paren_string):
    """ Remove the outer-most parentheses from a string. If it's already balanced, 
    then just return the string. Return None if there is no valid way to remove the parentheses. 
    
    For example:
        - "()" should return "None" because you cannot remove just one paren
        - "(())"