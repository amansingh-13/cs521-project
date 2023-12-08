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

I'm going to ask for both solutions to this problem. If you feel that the solution is unclear, don't hesitate to leave a question in the comment box and I will provide more clarification or alternative solutions. Be sure to include your name in your submission (unless you don't want to be identified).

Here's another example of a postcondition:
```def mean(num_list):
    assert len(num_list) >= 1, "Need at least one number"
    return sum(num_list)/len(num_list)```
It has an assert statement and a variable check that the function input is not empty. It's not as complicated as mean_absolute_deviation(), but it still encapsulates an aspect of the function without implementing it. The point of these exercis