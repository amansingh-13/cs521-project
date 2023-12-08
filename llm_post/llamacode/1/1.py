from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # TODO: Add your code here
    pass


def paren_balance_checker(input_string: str) -> bool:
    """ This function checks that a string containing parentheses is balanced. Return True if the string is balanced, False otherwise.
    >>> paren_balance_checker('( ) (( )) ((())))')
    True
    >>> paren_balance_checker('( (()()())(()))))')
    False
    """
    # TODO: Add your code here
    pass


def paren_matcher(left, right):
    """ This function checks if parentheses are balanced. Return True if the string is balanced, False otherwise.
    >>> paren_matcher('( ) (( )) ((())))')
    True
    >>> paren_balance_checker('( (()()())(()))))')
    False
    """
    # TODO: Add your code here
    pass


def is_valid_parentheses(input_string):
    """ Check if a string containing parentheses is valid. A string contains valid parentheses if each left parenthesis has a matching right parenthesis, and left parenthesis are properly nested to avoid mismatching right parenthesis in the correct location. Additionally, ignore any spaces in the input string.
    >>> paren_balance_checker('( ) (( )) ((())))')
    True
    >>> paren_balance_check