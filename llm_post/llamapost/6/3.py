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
Do not use any variables other than those in the function parameters or the return value (if present) to implement the postcondition.
For your purpose, the following functions are considered external: abs, max, sum, map, filter, list, all, any, zip
Note that the return value is called 'return_val' and should be used appropriately in your code for this question. Assume that parse_nested_parens has no side effects and no output other than its return value.
If you have any questions about the above postcondition, please ask them on piazza.

# Solution 1:

```python
def assert_all_nested_parens_are_balanced(return_val):
    '''
        The result list must match the nesting levels of parentheses in the input string, otherwise it is not a valid output.
    '''
    # ...
    # your code here
    # ...
```

# Solution 2:

```python
def assert_that_there_are_no_empty_strings(return_val):
    '''
        There must be no empty strings in the result list, otherwise it is not a valid output.
    '''
    # ...
    # your code here
    # ...
```
# Solution 3:

```python
def assert_that_the_result_list_is_ordered(return_val):
    '''
        The result list must be ordered in the same way as the input string, otherwise it is not a valid output.
    '''
    # ...
    # your code here
    # ...
```
# Solution 4:

```python
def assert_that_the_input_string_was_