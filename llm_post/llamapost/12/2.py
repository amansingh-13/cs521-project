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

You may find this link useful in learning about python types: http://mypy-lang.org/

> Solution:

```python 3
def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty."""
    
    if len(strings) == 0:
        return None
    
    max_len = 0
    res: Optional[str] = None
    
    for s in strings:
        if len(s) > max_len:
            max_len = len(s)
            res = s
            
    return res
```

> Solution to the postcondition:  
  ```assert (max_length == 0 and result == None or len(result) == max_length)```

### Partial Functional Subset of Python

What follows is an incomplete list of python type annotations. The goal here is not to provide comprehensive coverage but instead to get you started with the concepts. You should be able to annotate types in your code by following this list. In addition, this list can serve as a reference for understanding other libraries that support dynamic typing.
- int: integral number
- float: real number
- str: string
- list[T]: list of type T
- dict[K, V]: dictionary with keys of type K and values of type V
- Callable[[], R] : function taking no arguments and returning type R
- Optional[T]: the type Optional[T] represents an optional value - a value that may or may not be