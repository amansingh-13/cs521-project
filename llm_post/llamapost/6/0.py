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
The one assert statement in your postcondition should be sufficient to prove the postcondition, but you may add additional assertions if they aid in the proof. You may not use any loops (for/while). In general, the more you can get done with just a single assert, the better. If you are unsure how many asserts is 'good enough' for your postcondition, aim for 2.
If you have multiple postconditions, you should write separate functions for each one.
For further practice on writing symbolic postconditions, see:
https://www.udacity.com/course/programming-with-python-unit-tested--ud511
"""

from typing import List, Any
import collections

def parse_nested_parens(par