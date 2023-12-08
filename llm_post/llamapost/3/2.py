You have the following code context, function stub and natural language specification (in the form of a code comment) for below_zero. When implemented, the function should comply with this natural language specification:
from typing import List


def below_zero(operations: List[int]) -> bool:
    """ You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of account fallls below zero, and
    at that point function should return True. Otherwise it should return False.
    >>> below_zero([1, 2, 3])
    False
    >>> below_zero([1, 2, -4, 5])
    True
    """

Write a symbolic postcondition for below_zero consisting of exactly one assert statement. For variables, use only the function input parameters and a hypothetical return value, which we'll assume is stored in a variable return_val. If the postcondition calls any functions external to the program context, they should only be those from the functional subset of python. Although the postcondition should be less complex than the function itself, it should not be trivial. It should encapsulate an aspect of the function without implementing the function. The format of your response should be:
```CODE FOR EXACTLY ONE POSTCONDITION WITH ASSERT HERE```

Write a specification for below_zero consisting of exactly one postcondition, function preconditions and a test case in a code comment following the natural language specification. Your specification should be as close to the one presented above as possible. To determine whether your specification is sufficiently expressive, compare it with below_zero's natural language specification in the form of a code comment:
```CODE FOR EXACTLY ONE SPECIFICATION WITH PRECONDITIONS AND POSTCONDITION HERE```

Write a unit test for the postconditions of the function below_zero. The format of your response should be:
```UNIT TESTS FOR THE FUNCTION BELOW HERE, INCLUDING PRECONDITIONS AND ASSERTIONS FOR ALL POSTCONDITIONS```
"""
from typing import List


def below_zero(operations: List[int]) -> bool:
    """ You're given a list of integers where each integer represents the amount by which to change an account balance at that index. If the balance is negative, the operation would reduce the account balance below 0 and thus should be skipped. The function returns whether any of the operations resulted in a negative balance.
    >>> balance = [50]
    >>> below_zero(balance)
    False
    """
    return any(a < 0 for a in operations)


def below_zero_specification() -> None:
    def balances_never_negative() -> None:
        assert not below_zero([1, 2])
        assert not below_zero([3, -4])
        assert not below_zero([-50, 60])
