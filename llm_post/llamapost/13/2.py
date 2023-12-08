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

For example:
```python
def greeting(name):
    """ Output a personalised greeting for a person's name
        >>> greeting('Rick')
        'Hi, Rick!'
    """
    return 'Hi, ' + name + '!'

assert greeting('Morty') == "Hi, Morty!", \
       "Greetings mortal! You have been given a gift by your creator!"
```

Do not worry about the output to be correct with respect to natural language. It should be a valid python program that can be pasted into an interpreter or compiled and run as expected. The code should not contain any error messages, but it may contain warnings. It should have no syntax errors.

Ans:
```python
def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
        >>> assert (greatest_common_divisor(3, 5) == 1), "Greatest common divisor should be one"
    """
    return 1
```

### Problem 7.2: Postcondition with function call

A postcondition is a guarantee that the caller of your method/function will always receive correct output based on the inputs. It should be a valid python program that can be pasted into an interpreter or compiled and run as expected, but it may contain warnings.

Use this code below to help you complete Problem 7.2:
```python
def factorial(number: int) -> int:
    """ Returns the factorial of a number
        >>> assert factorial(6) ==