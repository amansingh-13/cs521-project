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
You should also include a code comment giving the specification to each postcondition in this response, along with an explanation justifying why that specific postcondition is sufficient to ensure correctness. Here's how you would write it for rolling_max:
postcond(return_val == [1, 2, 3, 3, 3, 4, 4])
# The output matches the natural language specification in the code comment above

Now we will implement your function. You may not refer to other functions or modules within this implementation; only those that are provided by python. Please use your best judgement and common sense when making decisions about how this postcondition is verified. Here's a skeleton implementation of rolling_max for you to fill in:
```CODE FOR IMPLEMENTATION AND PARTIAL POSTCONDITION HERE```

To see if we passed, run `python3 postconditions/test2.py`.

### Postcondition Test 3 (Testing the Code)
Write a natural language specification for the code for rolling_dice_with_bias above using only natural language. Here's what your response should look like:
```NATURAL LANGUAGE SPECIFICATION HERE```
You may refer to the python documentation if you don't know how to do something, but please explain in detail why you are doing it this way, and not some other way that also works. Here's how you would write it for rolling_dice_with_bias:
To roll a 6-sided die, the return value must be between 1 and 6 inclusive, with probability 4/9 of returning 1, an equal probability of 2,