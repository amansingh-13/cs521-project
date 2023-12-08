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
You can also reference a function from the unit test.


### 1.0 (20 points)
```python
import math
def is_prime(number : int) -> bool:
    if number == 1 or number % 2 == 0 and number != 2: # if it's not prime
        return False
    else:
        for divisor in range(3,int(math.sqrt(number))+1,2): # all odd numbers up to sqrt n
            if (number % divisor) == 0:
                return False
        return True
```
Write a symbolic postcondition for is_prime consisting of exactly one assert statement. For variables, use only the function input parameters and a hypothetical return value, which we'll assume is stored in a variable return_val. If the postcondition calls any functions external to the program context, they should only be those from the functional subset of python. Although the