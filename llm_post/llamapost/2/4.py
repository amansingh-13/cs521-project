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

Note that you may call `assert_equal` or `assert_almost_equal` to compare two numbers in a postcondition. If either of those is too verbose for your needs, then it is ok to assert the equality with equality operators (== and !=). In fact, if you want to be extra-cautious about comparing floats, you can use `assert abs(a - b) < 1e-7`.

```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """

    return  # CODE FOR EXACTLY ONE POSTCONDITION WITH ASSERT HERE, USING assert_equal
```

Now write another symbolic postcondition for truncate_number that involves more than one assertion. You may use `assert_almost_equal`, but if you want to be extra-cautious about comparing floats, then you can use `assert abs(a - b) < 1e-7`.

```python
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.