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
You may include any number of other assertions if they help clarify or make it easier to understand.
"""
def string_xor(a: str, b: str) -> str:
    return_val = ''
    for i in range(max(len(a), len(b))):
        if i < len(a) and i < len(b):
            assert return_val[i] ^ a[i] == b[i], f'The postcondition is violated here, at a[{str(i)}]: {return_val[i]} ^ {a[i]}'
        elif i < len(a):
            assert return_val[i] == a[i], f'Postcondition is violated here, at a[{str(i)}]: {return_val[i]}'
        else:
            assert return_val[i] ^ b[i] == 0, f'The postcondition is violated here, at b[{str(i)}]: {b[i]}'
    return return_val
assert string_xor('1', '5') == '4', 'Postcondition is violated at index 2 for the first condition.'
assert string_xor('10', '35') == '34', 'Postcondition is violated at index 3 for the second condition.'
# 7
"""Write a function, my_filter(my_list, condition), that returns a new list containing only
the elements of a given list for which some operation returns True. For example, if condition
is lambda x: x % 2 == 0 then the function should return [0, 2, 4, 6, 