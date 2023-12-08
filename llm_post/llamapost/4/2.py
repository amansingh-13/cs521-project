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
### 1.2: Finding the Mean Absolute Deviation (MAD) for a given array of numbers
Write a docstring comment and code that calculates mean absolute deviation for an array of numbers. If your function is called mean_absolute_deviation, it should take one input argument as a list of floats. You may assume the following:
```
1. all arguments are valid and finite (no infinite or NaNs)
2. all elements in the list are valid floating-point numbers
3. no element is a NaN
4. all elements are non-Negative
5. the mean of these numbers is valid and finite, and is not an invalid or NaN
```
Your function should return a float to be stored as a variable called answer. The value stored in this variable will be used by other functions later in your project, so it can't be written inline:
```
answer = mean_absolute_deviation(array)
```
The mean absolute deviation for an array of numbers is the average distance from the mean to the elements in the array. If you don't recall how to calculate this, [this wikipedia page](https://en.wikipedia.org/wiki/Average_absolute_deviation#Definition) will help. Include a docstring comment for your function that explains what it does and include an example of the function in use to get you 2 points (10% of final grade). To calculate this in code, you can take advantage of the following:
```
import numpy as np
mean = np.mean(numbers)
np.abs(np.subtract(mean, numbers)) # Returns an array of absolute differences between mean and numbers
np.sum(np.abs(np.subt