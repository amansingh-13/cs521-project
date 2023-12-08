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
"""

def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """

    # PRECONDITIONS:
    assert isinstance(number, float), "the input must be a float"
    assert 0 < number < np.inf, "The function must take positive numbers"

    if abs(number) > 1:
        return truncate_number(number/10) * 10
    else:
        return number % 1

# POSTCONDITIONS:
# assert isinstance(return_val, float), "the output must be a float"
assert abs(return_val) < 1, "the decimal part must be less than one."
# assert np.isclose(number, return_val + truncate_number(number)), "number must equal the fractional part added with the integer part."
# assert return_val > 0 and number > 0 or return_val < 