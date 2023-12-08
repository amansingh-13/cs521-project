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

To aid you in writing this postcondition, I've provided a hint as to what might be a suitable variable to use for the return value.

### Hint 

Remember, we do not need an assert statement that will evaluate to True because such a statement is always true. However, it would be better if we didn't have one of those either! Instead of a trivial assertion, you should use one that tests whether the return value and the greatest_common_divisor function are indeed equal when applied on some specific input values.
"""

import os 
os.system("mkdir -p results")

def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    if a == b:
        return a
    elif a > b:
        for i in range(a):
            if a % i == 0 and b % i == 0:
                return i
    elif a < b:
        for i in range(b):
            if a % i == 0 and b % i == 0:
                return i
    
print("greatest_common_divisor(3,5)")
print(greatest_common_divisor(3,5))
print("greatest_common_divisor(25,15)")
print(greatest_common_