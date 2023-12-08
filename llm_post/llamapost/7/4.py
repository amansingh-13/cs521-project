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
and you should use a code block for any functions in the postcondition.
## Answer
```python
# Postcondition: List containing only elements that contain substring
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    assert isinstance(strings, list) and \
        all(isinstance(element, str) for element in strings), "Input param 'strings' must be a list of strings."
    
    return [element for element in strings if substring in element]
```

## Comments
The postcondition is quite easy to understand. It says that the function will take a `List[str]` and returns a `List[str]`. But it adds more semantics to what a "containing" looks like. Instead of just checking whether the string contains the sub-string, the filter checks for a specific starting index (for example, after the first character). It is this specificity that makes the postcondition useful in addition to the previous one.

### Code Blocks vs. Plain Text
Because we are describing "what happens", it was better to use a code block than plain text. The reason for this is because if I had written:
```py
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    assert isinstance(strings, list) and \
        all(isinstance(element, str) for element in strings), "Input param 'strings' must be a list of strings."
    return [element for element in strings if substring in element]
```
The second line would have been interpreted as part of the postcondition instead of as code. It is very important to use code blocks with postconditions because it is more readable that way