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

```python
# def truncate_number(number): ...
def _assert_truncate_number_postcondition():
    assert False # insert code here!

_assert_truncate_number_postcondition()
```

<details> <summary>Answer</summary>

```python
# def truncate_number(number: float) -> float: ...
def _assert_truncate_number_postcondition():
    assert truncate_number(3.5) == 0.5, 'postcondition failed for argument number=3.5'

_assert_truncate_number_postcondition()
```
</details>

---
### [Return Value of max](https://www.practicepython.org/exercise/2014/12/19/return-value-of-max.html)
Write a code comment explaining the return value of max when applied to the following sequence: [3, 5, 8, 10, 7]. The format of your response should be ```CODE EXPLANATION HERE```
```python
# [3, 5, 8, 10, 7] ...
_assert_max_return_value() # explain return value here!
```
<details> <summary>Answer</summary>

The function returns the largest of its arguments. This case means that it will return the value of 10 since it is greater than all other values in the sequence.
</details>

---
### [Square Root](https://www.practicepython.org/exercise/2014/12/19/square-root.html)
