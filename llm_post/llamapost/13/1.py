You have the following code context, function stub and natural language specification (in the form of a code comment) for greatest_common_divisor. When implemented, the function should comply with this natural language specification:


def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """

Write a symbolic postcondition for greatest_common_divisor consisting of exactly one assert statement. For variables, use only the function input parameters and a hypothetical return value, which we'll assume is stored in a variable return_val. If the postcondition calls any functions external to the program context, they should only be those from the functional subset of python. Although the postcondition should be less complex than the function itself, it should not be trivial. It should encapsulate an aspect of the function without implementing the function. The format of your response should be:
```CODE FOR EXACTLY ONE POSTCONDITION WITH ASSERT HERE```
You will provide your code in a file called solutions/greatest_common_divisor.py and your test case for the postcondition should be written into the file tests/test_greatest_common_divisor.py
'''

def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    return_val = None
    if type(a) != int or type(b) != int:
        raise TypeError("Inputs must be integers")
    if a < 0:
        raise ValueError("Input cannot be negative")
    if b < 0:
        raise ValueError("Input cannot be negative")
    # base cases 1 and 2
    if a == b:
        return_val = a
    elif a > b:
        return_val = gcd_helper(a, b)
    else:
        return_val = gcd_helper(b, a)
    assert isinstance(return_val, int) and return_val >= 1
    return return_val

def gcd_helper(a: int, b: int) -> int:
    """ Returns a gcd of integers a and b"""
    # base case 3 (if they are both even)
    if a % 2 == b % 2 == 0:
        return gcd_even_helper(a, b)
    # base case