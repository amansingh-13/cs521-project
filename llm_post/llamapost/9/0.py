You have the following code context, function stub and natural language specification (in the form of a code comment) for rolling_max. When implemented, the function should comply with this natural language specification:
from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """

Write a symbolic postcondition for rolling_max consisting of exactly one assert statement. For variables, use only the function input parameters and a hypothetical return value, which we'll assume is stored in a variable return_val. If the postcondition calls any functions external to the program context, they should only be those from the functional subset of python. Although the postcondition should be less complex than the function itself, it should not be trivial. It should encapsulate an aspect of the function without implementing the function. The format of your response should be:
```CODE FOR EXACTLY ONE POSTCONDITION WITH ASSERT HERE```

Example:
>>> def my_function(a: int, b: int) -> int:
...     "Returns the value at index 'a + b' in a list of 10 numbers."
...     return my_list[a+b]
...
... assert isinstance(my_function(5, 7), int), "Output must be an integer!"
>>> my_function(5, 7)
8
You can use the following code to test your postcondition. Make sure the postconditions are in a separate file from the function you're testing (for this, create a file called test_my_function.py). The doctest line should be added to the bottom of your postcondition:
```doctest
>>> import doctest
>>> doctest.testmod(verbose=True)
****************************************************************