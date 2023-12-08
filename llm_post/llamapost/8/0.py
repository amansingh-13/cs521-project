You have the following code context, function stub and natural language specification (in the form of a code comment) for sum_product. When implemented, the function should comply with this natural language specification:
from typing import List, Tuple


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    """

Write a symbolic postcondition for sum_product consisting of exactly one assert statement. For variables, use only the function input parameters and a hypothetical return value, which we'll assume is stored in a variable return_val. If the postcondition calls any functions external to the program context, they should only be those from the functional subset of python. Although the postcondition should be less complex than the function itself, it should not be trivial. It should encapsulate an aspect of the function without implementing the function. The format of your response should be:
```CODE FOR EXACTLY ONE POSTCONDITION WITH ASSERT HERE```

The code should include type annotations for any variables you need to define and return, in the following format, where NUMBER is a variable name, TYPE is a data type or another function call.
```python3
def NAME(TYPE NUMBER):
    '''SHORT DESCRIPTION'''
    ASSERTION
    RETURN VALUE
    '''LONGER BRIEFIER DESCRIPTION'''
```
As usual, please use the python interpreter to test your solution. Feel free to ask us questions on Slack if you get stuck.

###### Solution:
```python3
def sum_product(numbers: List[int]) -> Tuple[int, int]:
    '''The sum and product of a list of integers'''
    return_val = (0, 1)
    assert isinstance(return_val, Tu