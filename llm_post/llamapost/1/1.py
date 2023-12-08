You have the following code context, function stub and natural language specification (in the form of a code comment) for separate_paren_groups. When implemented, the function should comply with this natural language specification:
from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

Write a symbolic postcondition for separate_paren_groups consisting of exactly one assert statement. For variables, use only the function input parameters and a hypothetical return value, which we'll assume is stored in a variable return_val. If the postcondition calls any functions external to the program context, they should only be those from the functional subset of python. Although the postcondition should be less complex than the function itself, it should not be trivial. It should encapsulate an aspect of the function without implementing the function. The format of your response should be:
```CODE FOR EXACTLY ONE POSTCONDITION WITH ASSERT HERE```
and should also include your code comment for this postcondition.

The following are some examples of assert expressions which would make good postconditions:
- return_val is an empty list if paren_string is an empty string. This is a trivial postcondition.
- The length of the return_val is equal to the number of parentheses in paren_string.
- All elements in return_val are strings starting with '(' and ending with ')'.

Here's your symbolic postcondition:
```
assert all(group[0] == '(' and group[-1] == ')' for group in return_val)
```

# Hints
- The first thing you should do when writing a postcondition is to make sure it makes sense!
- You can create any number of assert statements. They will all be evaluated together. If you write multiple assertions, you must use the `and` operator to combine them.
- There is a special function called `all()` which takes an iterable and returns whether or not every element in the iterable evaluates to true. The following example illustrates how it works:
```python
nums = [1, 2, 3]
assert all(num % 2 == 0 for num in nums)
```
Here, we check if any number is odd and return False if so because one of the elements evaluates to false. But what happens if we change our code a little?
```python
nums = [1, 2, 3]
assert all(num % 2 == 0 for num in nums)
```
Now all of the numbers are even but the first element is still odd so the length of the iterable is greater than one and the function `all()` returns true.
- In this case