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

### 6.05

The following code snippet is a stub for a function that calculates and returns the length of its argument. Write one or more symbolic postconditions for this function, each in the form of an assert statement using only the return value, its input arguments (if any), and hypothetical values for local variables.
```python
def length(s):
    """ Return length of string s.
    :param str s: The string to measure.
    :return: Length of string s.
    :rtype: int
    """
```
### 6.06

The following code snippet is a stub for a function that compares two strings and returns -1 if one is less than the other, or 0 if they are equal, or 1 if one is greater than the other. You should write one symbolic postcondition for the function in the form of an assert statement using only the return value, its input arguments (if any), and hypothetical values for local variables.
```python
def cmp(s1, s2):
    """ Compare two strings.
    :param str s1: The first string to compare.
    :param str s2: The second string to compare.
    :return: -1 if s1 is less than s2; 0 if the strings are equal; 1 if s1 is greater than s2.
    :rtype: int
    """
```
### 6.07

The following code snippet is a stub for a function that computes and returns the sum of two numbers. Write one or more symbolic postconditions for this function, each in the form of an assert statement using only the