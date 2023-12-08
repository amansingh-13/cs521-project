You have the following code context, function stub and natural language specification (in the form of a code comment) for parse_nested_parens. When implemented, the function should comply with this natural language specification:
from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

Write a symbolic postcondition for parse_nested_parens consisting of exactly one assert statement. For variables, use only the function input parameters and a hypothetical return value, which we'll assume is stored in a variable return_val. If the postcondition calls any functions external to the program context, they should only be those from the functional subset of python. Although the postcondition should be less complex than the function itself, it should not be trivial. It should encapsulate an aspect of the function without implementing the function. The format of your response should be:
```CODE FOR EXACTLY ONE POSTCONDITION WITH ASSERT HERE```
For example:
assert len(return_val) == 0
"""

def parse_nested_parens(paren_string):
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.
    
    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    return_val = []

    for paren in paren_string.split():
        max_num = 0
        count = 0
        for char in paren:
            if char == "(":
                count += 1
                if max_num < count:
                    max_num = count

            elif char == ")":
                count -= 1
        
        return_val.append(max_num)
    
    return return_val

assert len(parse_nested_parens("")) == 0
assert parse_nested_parens("(()())")[0] == 2
assert parse_nested_parens("()()()")[1] == 3
assert len(parse_nested_parens("((()))()()()")) == 6
assert parse_nested_parens("((()))()()()")[5] == 4
assert parse_nested_parens("((()))()()()")[0] == 2

"""
Please write a function called `find_odd_numbers