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

### Part 3: Greater_common_divisor
Given a context of:


def greatest_common_divisor(a, b):
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """

Write one postcondition for this function that uses only the function stub. No more than two assert statements are allowed in a postcondition.
```CODE FOR ONE POSTCONDITION WITH ASSERTS HERE```

Write another postcondition for this function, and then write your third postcondition, which is different from the first two in some way (either by using new variables or asserting different things).
```CODE FOR SECOND POSTCONDITION WITH ASSERT HERE```

### Part 4: Implementing a Postcondition
Implement one of your postconditions. The function should be implemented to comply with the natural language specification you wrote in Part 1.

Define a function named greater_common_divisor that takes two positive integers as arguments and returns an integer such that it is the greatest common divisor.
```CODE FOR FUNCTION DEFINITION HERE ```

### Part 5: Implementing Another Postcondition
Implement your other postcondition. The function should be implemented to comply with the natural language specification you wrote in Part 1.

Define a function named greater_common_divisor that takes two positive integers as arguments and returns an integer such that it is the greatest common divisor.
