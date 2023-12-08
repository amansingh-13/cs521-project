from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # TODO: Implement this function!
    return []


def is_valid_parentheses(paren_string: str) -> bool:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to determine
    if that group is balanced and not nested within each other. Ignore any spaces in the input string.
    >>> is_valid_parentheses('(( ) (( )) (( )( )))')
    True
    """
    # TODO: Implement this function!
    return False


def get_paren_counts(paren_string: str) -> int:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to determine
    the number of opening and closing parentheses in that group. Ignore any spaces in the input string.
    >>> get_paren_counts('(( ) (( )) (( )( )))')
    6
    """
    # TODO: Implement this function!
    return -1


def get_longest_group(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to determine
    the longest group of balanced parentheses within that string. If there are two or more groups which have the same
    length, return the one that opens first. Ignore any spaces in the input string.
    >>> get_longest_group('(( ) (( )) (( )( )))')
    '()'
    """
    # TODO: Implement this function!
    return