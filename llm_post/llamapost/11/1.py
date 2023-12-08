You have the following code context, function stub and natural language specification (in the form of a code comment) for string_xor. When implemented, the function should comply with this natural language specification:
from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """

Write a symbolic postcondition for string_xor consisting of exactly one assert statement. For variables, use only the function input parameters and a hypothetical return value, which we'll assume is stored in a variable return_val. If the postcondition calls any functions external to the program context, they should only be those from the functional subset of python. Although the postcondition should be less complex than the function itself, it should not be trivial. It should encapsulate an aspect of the function without implementing the function. The format of your response should be:
```CODE FOR EXACTLY ONE POSTCONDITION WITH ASSERT HERE```


**Note:** This is not a homework problem. You do not need to write a solution, you merely must describe one in comments. 

### Answer

The postcondition is that the output string consists only of '0's and '1's. So:
```python
post = assert all(x == '0' or x == '1' for x in return_val)
```

**Note** The first line of this answer was copied verbatim from the comments section of the problem statement, and the second line is not a valid Python expression.

## Problem 3 (5 points):

The following code snippet defines a function that takes a string and returns a new string consisting of all of its characters in reverse order:
```python
def reverse(s: str) -> str:
    return ''.join(reversed(s))

print(reverse('hello world'))
```
Write the symbolic postcondition for this function consisting of exactly one assert statement. Your answer should not refer to any values other than those passed as parameters and the hypothetical value returned by the function. 
Your answer should be a valid Python expression, but should not execute.
You may use multiple statements, including assignment statements, if you wish. It is okay to define additional functions in your postcondition or solve problems from previous assignments (as long as they are not part of the same submission).
Do not submit this assignment; instead, please answer on Piazza by posting an image containing your code and your single assert statement.

**Hint:** You may find it useful to define another function that reverses a string using a list rather than calling `reversed()` directly in your postcondition. 

### Answer