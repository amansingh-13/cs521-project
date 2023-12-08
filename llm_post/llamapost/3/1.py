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
"""
from typing import List
# from unittest.mock import patch
import unittest


def below_zero(operations: List[int]) -> bool:
    """ You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of account fallls below zero, and
    at that point function should return True. Otherwise it should return False.
    >>> below_zero([1, 2, 3])
    False
    >>> below_zero([1, 2, -4, 5])
    True
    """
    balance = 0
    for operation in operations:
        if balance < operation:
            return True
        elif operation >= 0:
            balance += operation
    return False


class Test_below_zero(unittest.TestCase):

    def test_1(self):
        self.assertEqual(True, below_zero([1, 2, -4, 5]))

    def test_2(self):
        self.assertEqual(False, below_zero([3, 2, 8, -6]))

    def test_3(self):
        self.assertEqual(True, below_zero([-10, -1]))

    def test_4(self):
        self.assertEqual(False, below_zero([5, 6, 7, 8]))


if __name__ == "__main