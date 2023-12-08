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

The postcondition for parse_nested_parens is:
```assert '(' in paren_string if not all(x == ')' for x in paren_string) else True```
This checks that all elements of the input string are closing parentheses (i.e., '), as we don't want to accept strings with only opening parentheses like ()(). We can do this check after checking that there were no more than 3 levels of nesting, which is a postcondition for parse_nested_parens.

The postcondition says: If the string does not contain an opening parenthesis (i.e., '('), then the return value should be True.
This check is needed because the code might have issues with strings that are empty or contain only ')'s and we want to make sure they won't throw errors when we call parse_nested_parens().

The postcondition says: If the string contains any opening parenthesis, then there were more than 3 levels of nesting.
This check is needed because we are interested in numbers less than or equal to 3 and we want the function to throw an error when it encounters a case with more than 3 levels of nesting.

The postcondition says: If the string does not contain any closing parenthesis (i.e., '), then the number of opening and closing parentheses is equal, so there was no nesting. The return value should be True.
This check is needed because we don't want to accept strings with only opening parentheses like ()(). We want to make sure they won't throw errors when we call parse_nested_parens() and also that the function returns True when it doesn't encounter any nesting. If the string does not contain