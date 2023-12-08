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

#### 9a.
The postcondition for rolling_max is as follows:
```
assert (all(
    # In each case, rolling max should increase until the number being considered and then decrease again.
     # This means we must be at least as big as the number before.
        x >= y  # This statement is required to work
            for x, y in zip(return_val, numbers)
    )
    # After each increase, it will either remain the same or be smaller than the next element.
    and all(
        (
            x >= prev_x or
            # If it is smaller, then it can only decrease again if there was a previous max.
            prev_max is not None and y > prev_x
        )
        for x, y, prev_x, prev_max in zip(return_val, numbers, return_val[:-1], return_val[1:])
    )
)
```

#### 9b.
The postcondition for rolling_sum is as follows:
```
assert (all(
    # In each case, rolling sum should increase until the number being considered and then decrease again.
     # This means we must be at least as big as the number before.
        x >= y  # This statement is required to work
            for x, y in zip(return_val, numbers)
    )
    # After each increase, it will either remain the same or be smaller than the next element.
    and all(
        (
            x >= prev_x or
            # If it is smaller, then it can only decrease again if there was a previous max.
            prev_max is not None and y > prev