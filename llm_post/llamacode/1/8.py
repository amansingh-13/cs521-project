from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # +++your code here+++
    # If you pass all the test cases don't forget to return the result from your function
    # You can add new variables and do whatever you want
    stack = []
    ans_list = []
    for i in range(len(paren_string)):
        if paren_string[i] == '(':
            stack.append(1)
        elif paren_string[i] == ')':
            if len(stack) == 0 or stack[-1] != 1:
                return []
            stack.pop()
    # print("Stack length", len(stack))

    for i in range(len(paren_string)):
        ans = ""
        while stack and paren_string[i] == ')':
            ans += str(stack[-1])
            stack.pop()
            if stack:
                ans += str(stack[-1])
            else:
                break
        stack.append(paren_string[i])
        while stack and len(ans) < len(paren_string):
            ans +=