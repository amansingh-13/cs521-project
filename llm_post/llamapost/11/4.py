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
The following code will return True if the postcondition is satisfied (passes all tests):
```python
assert(string_xor('101', '111') == 
        string_postcondition('101', '111'))
```
Do not modify any of the other