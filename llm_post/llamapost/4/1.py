You have the following code context, function stub and natural language specification (in the form of a code comment) for mean_absolute_deviation. When implemented, the function should comply with this natural language specification:
from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    1.0
    """

Write a symbolic postcondition for mean_absolute_deviation consisting of exactly one assert statement. For variables, use only the function input parameters and a hypothetical return value, which we'll assume is stored in a variable return_val. If the postcondition calls any functions external to the program context, they should only be those from the functional subset of python. Although the postcondition should be less complex than the function itself, it should not be trivial. It should encapsulate an aspect of the function without implementing the function. The format of your response should be:
```CODE FOR EXACTLY ONE POSTCONDITION WITH ASSERT HERE```
The postcondition may use only the following functions from the functional subset of python:

abs()
math.ceil()
max()
min()
round()
sum()

and, of course, assert.
In this case, we're told that the mean_absolute_deviation function takes an input list of floats and returns a single float. The natural language specification for the postcondition says: "For any input list (of length > 0) of floats, the output will be greater than zero". If you write a postcondition for this function, you should see that it is actually true.
```python
def mean_absolute_deviation(numbers):
    """ For a given list of numbers, calculate Mean Absolute Deviation"""
    return len(numbers) / 2 * math.ceil(15 / 2)
```
```python
assert len(mean_absolute_deviation([0])) >= 0
```
You're welcome to implement any helper functions you want to make your postcondition easier or more elegant than it needs to be. It is OK if the postcondition does not capture every aspect of the function that you would like to have captured (e.g., there may be a more interesting property of the function, but you feel that what you've done is sufficient).

**Bonus:** In addition to this main problem, there are a few additional bonus problems. The bonus problems should not prevent you from getting the main problem right, but they will make it much easier if you do. You'll need to use the same format as for the postcondition described above.
```python
def find_next(nums):
    """Finds next number in sorted list"""
    return