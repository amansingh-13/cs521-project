You have the following code context, function stub and natural language specification (in the form of a code comment) for rolling_max. When implemented, the function should comply with this natural language specification:
from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence.
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """

Write a symbolic postcondition for rolling_max consisting of exactly one assert statement. For variables, use only the function input parameters and a hypothetical return value, which we'll assume is stored in a variable return_val. If the postcondition calls any functions external to the program context, they should only be those from the functional subset of python. Although the postcondition should be less complex than the function itself, it should not be trivial. It should encapsulate an aspect of the function without implementing the function. The format of your response should be:
```CODE FOR EXACTLY ONE POSTCONDITION WITH ASSERT HERE```
For example, a postcondition might look like:
assert len(numbers) == 0 or return_val != numbers[len(numbers)-1], "last number is not max"
In addition to providing an assert statement, please provide comments that describe what the postcondition checks.
'''

numbers = [1, 2, 3, 2, 3, 4, 2]
from typing import List
def rolling_max(numbers:List[int])->List[int]:
    """ From a given list of integers, generate a list of rolling maximum element found until given moment
    in the sequence. """
    output = []
    for number in numbers:
        if len(output) == 0 or number > output[-1]: # check if element is max
            output.append(number) # add to output
        else:
            pass # do nothing
    return output
assert len(numbers) == 0 or rolling_max(numbers)[len(numbers)-1] != numbers[len(numbers)-1], "last number not max"
# check if last element is not maximum of list
'''
def test_rolling_max():
    numbers = [1, 2, 3, 2, 3, 4, 2]
    assert len(numbers) == 0 or rolling_max(numbers)[len(numbers)-1] != numbers[len(numbers)-1], "last number not max"

def test_rolling_max_long():
    long_list = list(range(0,101))*2 + list(range(0,101))*3
    assert len(long_list) == 0 or rolling_max(long