You have the following code context, function stub and natural language specification (in the form of a code comment) for longest. When implemented, the function should comply with this natural language specification:
from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.
    >>> longest([])

    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    """

Write a symbolic postcondition for longest consisting of exactly one assert statement. For variables, use only the function input parameters and a hypothetical return value, which we'll assume is stored in a variable return_val. If the postcondition calls any functions external to the program context, they should only be those from the functional subset of python. Although the postcondition should be less complex than the function itself, it should not be trivial. It should encapsulate an aspect of the function without implementing the function. The format of your response should be:
```CODE FOR EXACTLY ONE POSTCONDITION WITH ASSERT HERE```

*Please include a brief description of what you did for the postcondition. We will read this in class.*

Here is my solution:
```python
def longest(strings : List[str]) -> Optional[str]:
  """Out of list of strings, return the longest one. Return the first one in case of multiple
  strings of the same length. Return None in case the input list is empty."""
  
  assert len([s for s in strings if len(s) > 0]) > 0
```

### Part 3 - Refactored with Postcondition Checks and No Exceptions ###

Now let's refactor the code to use postconditions. Here is a solution:

```python
from typing import List, Optional

def longest(strings : List[str]) -> Optional[str]:
    """Out of list of strings, return the longest one