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

Example postconditions for above_equal_zero include:
def above_equal_zero(operations: List[int]) -> bool:
    """ You're given a list of deposit and withdrawal operations on a bank account that starts with zero balance. Your task is to detect if at any point the balance of account stays equal or greater than zero, and in such a case return True. Otherwise it should return False.
    >>> above_equal_zero([1, 2, 3])
    True
    >>> above_equal_zero([1, -2, 5, -6])
    False
    """

Write a symbolic precondition for below_zero consisting of exactly one assert statement. For variables, use only the function input parameters and a hypothetical return value, which we'll assume is stored in a variable return_val. If the precondition calls any functions external to the program context, they should only be those used by above_equal_zero and above_zero. The format of your response should be:
```CODE FOR EXACTLY ONE PRECONDITION WITH ASSERT HERE```

Example preconditions for below_zero include:
def below_zero(operations: List[int]) -> bool:
    """ You're given a list of deposits and withdrawals on a bank account that starts with zero balance. Your task is to return True if the final balance is negative, and False otherwise.
    >>> below_zero([1, 2, 3])
    False
    >>> below_zero([-1, -2])
    True
    """

Write a symbolic postcondition for above_equal_zero consisting of exactly one assert statement. For