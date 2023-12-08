from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    open_brace = 0
    close_brace = 0
    start_index = 0
    # loop over all characters in the string
    for i, char in enumerate(paren_string):
        if (char == "("):
            open_brace += 1
        elif (char == ")"):
            close_brace += 1
        else:
            continue
        # check if the counts are balanced
        if (open_brace != close_brace):
            start_index = i + 1
            continue
        # if the values are balanced, add the substring to the list
        else:
            groups.append(paren_string[start_index : i])
            start_index = i + 1
    # add the last group to the list, if it exists
    if (open_brace == close_brace):
        groups.append(paren_string[start_index:])
    return groups


def main():
