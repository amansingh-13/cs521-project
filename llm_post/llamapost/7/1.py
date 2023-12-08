You have the following code context, function stub and natural language specification (in the form of a code comment) for filter_by_substring. When implemented, the function should comply with this natural language specification:
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring
    >>> filter_by_substring([], 'a')
    []
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    """

Write a symbolic postcondition for filter_by_substring consisting of exactly one assert statement. For variables, use only the function input parameters and a hypothetical return value, which we'll assume is stored in a variable return_val. If the postcondition calls any functions external to the program context, they should only be those from the functional subset of python. Although the postcondition should be less complex than the function itself, it should not be trivial. It should encapsulate an aspect of the function without implementing the function. The format of your response should be:
```CODE FOR EXACTLY ONE POSTCONDITION WITH ASSERT HERE``` 


The following code shows how to use mypy to catch type errors in filter_by_substring, and is also a good place to start if you want to test the postcondition yourself (before writing one).
```python
def my_type_test(x: int):
    return x + 1

my_type_test('string')
# error: Argument 1 to "my_type_test" has incompatible type "str"; expected "int"
```
## SOLUTION:
I'll go with:

```python
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring
    
    >>> filter_by_substring([], 'a')
    []
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    """
    def isIn(s1: str, s2: str) -> bool:
        if len(s2)>len(s1):
            return False
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                return False