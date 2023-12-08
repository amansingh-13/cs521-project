You have the following code context, function stub and natural language specification (in the form of a code comment) for intersperse. When implemented, the function should comply with this natural language specification:
from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """

Write a symbolic postcondition for intersperse consisting of exactly one assert statement. For variables, use only the function input parameters and a hypothetical return value, which we'll assume is stored in a variable return_val. If the postcondition calls any functions external to the program context, they should only be those from the functional subset of python. Although the postcondition should be less complex than the function itself, it should not be trivial. It should encapsulate an aspect of the function without implementing the function. The format of your response should be:
```CODE FOR EXACTLY ONE POSTCONDITION WITH ASSERT HERE```
"""
def post(numbers: List[int], delimeter: int) -> List[int]:
    """Assert that intersperse inserts a number 'delimeter' between every two consecutive elements of input list numbers."""
    
    # postcondition is the following assertion, but it's not in code form.
    assert all(output_val[i] == delimeter if i % 2 else output_val[i] == numbers[i // 2] for i, output_val in enumerate(output_val))
    
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)