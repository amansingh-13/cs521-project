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

### Postconditions
We can find out the mean of a list of numbers (the "centerpoint" for calculating MAD).
    ```assert np.allclose(return_val, np.mean(numbers))``` 

### Comments
The output should be a number, and it should not be zero.

# Exercise 1: 99 bottles
You can find this exercise [here](https://github.com/Make-School-Labs/BEW-2.2-Bouncing-Ducks/blob/master/python/bottle_counter.py).
### Comments
This program is not the bottles of beer song. It's a small modification to the original code, and it does one job - count down from 99 to zero.

As it stands, this program has two main functions (one of them is commented out) - a function that counts downwards, and another function that prints the number. They are both called by running bottles_of_beer(99), which counts down from 99 to zero. It should be noted that the print() method in Python 3 does not have an integer parameter. So the code that was written with Python 2 will not work in Python 3, because you cannot use "print" as a function (it's a special thing).
### Comments
The reason why it doesn't work is because you can't call print() like a function. This would have worked:
```for num in range(99, 0, -1):  
    if num > 1:  
        print(num, 'bottles of beer on the wall')