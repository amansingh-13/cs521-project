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

The following code should pass all tests when added to a file parse_nested_parens.py next to the function stub above:
def assertPostcondition(assertFunc):
    """A helper function for running assert statements. Takes an assert function as an argument and runs it, including any side-effects."""
    # Additional code here...

postcondition = ...

print(parse_nested_parens('(()()) ((())) () ((())()())'))  
# [2, 3, 1, 3]
assert assertPostcondition(postcondition)


You should submit a screenshot of the postcondition code in parse_nested_parens.py with the following comment: # POSTCONDITION HERE
"""[Insert description of what you are posting here.]"""

    # Additional code here...
    
# POSTCONDITION HERE
def assertPostcondition(assertFunc):
    """A helper function for running assert statements. Takes an assert function as an argument and runs it, including any side-effects."""
    # Additional code here...

postcondition = ...

print(parse_nested_parens('(()()) ((())) () ((())()())'))  
# [2, 3, 1, 3]
assert assertPostconditioncondition(postcondition)


You should submit a screenshot of the postcondition code in parse_nested_parens.py with the following comment: # POSTCONDITION CONDITION HERE
"""[Insert description of what you are posting here.]"""

    # Additional code here...
    
# POSTCONDITION CONDITION HERE
def assertPostcondition(