from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    def get_group(s, start):
        count = 0
        for i in range(start + 1, len(s)):
            if s[i] == ')':
                count -= 1
                if not count:
                    return ''.join(s[start:i + 1]), i + 1
            elif s[i] == '(':
                count += 1
        return None, start

    groups = []
    for s in paren_string.split():
        curr_group, curr = get_group(s, 0)
        while curr < len(s):
            new_group, start = get_group(s, curr)
            if new_group is not None:
                groups.append(new_group)
            else:
                break
            curr = start
    return groups

