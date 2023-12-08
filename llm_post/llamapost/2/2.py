You have the following code context, function stub and natural language specification (in the form of a code comment) for truncate_number. When implemented, the function should comply with this natural language specification:


def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """

Write a symbolic postcondition for truncate_number consisting of exactly one assert statement. For variables, use only the function input parameters and a hypothetical return value, which we'll assume is stored in a variable return_val. If the postcondition calls any functions external to the program context, they should only be those from the functional subset of python. Although the postcondition should be less complex than the function itself, it should not be trivial. It should encapsulate an aspect of the function without implementing the function. The format of your response should be:
```CODE FOR EXACTLY ONE POSTCONDITION WITH ASSERT HERE```

You can use any of the following symbols for assert in this context:
```assert, Assert, AssertionError, asser, aseert, ```

Your postcondition should not have side effects (no print statements) and it should return a Boolean value.

For example, the following is an acceptable postcondition that may be used to test your implementation of truncate_number:
```
assert(return_val==truncate_number(3.5))
```

You may use any other names you like for the input and return values; however, they should clearly indicate their role in the postcondtion. The following are examples that would also be acceptable:
```
def assert_truncate_number(num):
    """Assert that the return value of truncate_number is equal to num's decimal part."""
    assert(truncate_number(3.5)==3.5)
```
```
assert len(truncate_number('1')) == 0
```
```
def assert_decimal_part_of_number(num):
    """Assert that the decimal part of num is equal to the return value."""
    # the return value will be a float or an int, depending on the argument.
    assert(truncate_number(num) == num%1)
```
If you are confused about how to do this, please check your notes and work with your TA if necessary.

HINT: This is a good time for you