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
Then paste your symbolic postcondition in as follows:
```python
    >>> assert a == '01' and b == '11' and return_val == '10' # This is where you paste the postcondition.
     * check_sat
     * assertion failed at line 24, column 25 to line 124, column 9:
        AssertionError: assert False
```
Now test your postcondition by calling the function with these inputs:
```python
    string_xor('01', '11')
```
If this is working correctly, you will get an assertion error. If not, re-check your implementation of string_xor and postcondition until it does work. When you have finished testing your postcondition, paste the result in as follows:
```python
>>> assert a == '01' and b == '11' and return_val == '10' # Your Post-Condition here.
 * check_sat
 * assertion failed at line 24, column 25 to line 124, column 9:
    AssertionError: assert False
```
Now you can move on to the next problem. If you do not understand how to get your postcondition working, ask for help by adding a comment to this problem's Github issue page and ping @njzulrich.

## Problem 2
Your second task is to implement a version of string_contains that takes two strings and returns true if the first string contains the substring of characters in the second string, false otherwise. We will use this later to implement an implementation of fuzzy-search in python that finds all the words in a dictionary that match