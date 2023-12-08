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
## Response
```python
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring
    >>> a = ['abc', 'bacd', 'cde', 'array']
    >>> b = ['abcd','cde', 'a', 'array']
    >>> c = ['abc','bcda', 'cde', 'a', 'array']
    
    >>> filter_by_substring(a, 'a') == a
    True
    >>> filter_by_substring(b, 'a') == ['abcd','array']
    True
    >>> filter_by_substring(c, 'a') == ['abc', 'bcda', 'array']
    True
```
### Answers
We could use postcondition from the previous question. I am not sure how to do it with a function stub.
```python
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    >>> filter_by_substring(['abcd', 'cde', 'a', 'array'], 'a') == ['abcd','array']
    True
    """
```
### Answers
```python
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a') == ['abc', 'bacd', 'array']
    True
    >>> filter_by_substring(['abcd', 'cde', 'a', 'array'], 'a')