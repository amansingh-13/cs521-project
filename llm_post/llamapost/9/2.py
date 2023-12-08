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

Here is the code context for this exercise.

    from typing import List, Tuple
    
    def rolling_max(numbers: List[int]) -> List[int]:
        """ From a given list of integers, generate a list of rolling maximum element found until given moment
        in the sequence.
        
        >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
        [1, 2, 3, 3, 3, 4, 4]
    
        """
        return []

```
from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 4, 4]
    
    """
    return []
```

Here is the code context for this exercise.

    from typing import List, Tuple
    
    def rolling_max(numbers: List[int]) -> List[int]:
        """ From a given list of integers, generate a list of rolling maximum element found until given moment
        in the sequence.
        
        >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
        [1, 2, 3, 3, 4, 4]
    
        """
        return []
```

Here is the code context