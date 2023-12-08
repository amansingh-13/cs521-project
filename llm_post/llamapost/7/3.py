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

### Context
Write your context here. No more than 3 paragraphs (each containing at most 25 lines). Your answer must satisfy all of the following:
* You must have written, tested and handed in another function for this exercise that uses filter_by_substring
* The test for that other function should be less trivial and more complex than the one for filter_by_substring.
* This exercise cannot simply replicate the previous exercise or be an exercise that is not conceptually different from the previous exercise.
* You must give a very clear, detailed natural language description of why this context makes the problem interesting.

### Function Stub and Natural Language Specification
Write your function stub here, followed by a natural language specification in the form of a code comment. The spec should be at least 20 characters long but no more than 50 characters. Your answer must satisfy all of the following:
* It should contain a variable named `strings` with type `List[str]` and a variable named `substring` with type `str`.
* Your stub is exactly the same as in the previous exercise, except that it contains at most one character less than your spec.
* Your spec should be at least 20 characters long but no more than 50 characters.
* The function should make use of exactly one built-in function from the `builtins` package (imported as `builtins`). That built-in function must have either a single argument or two arguments with types matching the types specified in your stub, and that built-in function should return a `List[str]`.
* Your spec should contain at least one sentence.
* You must give a very clear, detailed natural language description of why this function stub makes the problem interesting.

