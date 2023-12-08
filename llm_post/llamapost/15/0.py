You have the following code context, function stub and natural language specification (in the form of a code comment) for string_sequence. When implemented, the function should comply with this natural language specification:


def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    """

Write a symbolic postcondition for string_sequence consisting of exactly one assert statement. For variables, use only the function input parameters and a hypothetical return value, which we'll assume is stored in a variable return_val. If the postcondition calls any functions external to the program context, they should only be those from the functional subset of python. Although the postcondition should be less complex than the function itself, it should not be trivial. It should encapsulate an aspect of the function without implementing the function. The format of your response should be:
```CODE FOR EXACTLY ONE POSTCONDITION WITH ASSERT HERE```

``` python
assert return_val == ' 0  1   2  3  4  5  6  7  8  9  10  11'
```

### Problem 3(b) 
Write a solution for the problem above. You may write additional code outside of the function as well as functions in addition to the function stub above, but be sure that you implement only the function and its postcondition.

```python
def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    """

    assert "not implemented" == "not implemented"
```

### Problem 4
Consider the following code context:
```python
def main():
   