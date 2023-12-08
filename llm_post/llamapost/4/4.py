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
(the quotes are required). 
Do not use the keyword assert or the return statement.


I've been thinking about what a postcondition might be, and it occurred to me that I may need to think of these in the context of "invariant" (what is not changing), which might make things simpler?


If this were a real application, there are several important invariants:
1. Return value is a number 0 <= x <= 1 (if no nulls or infs). The lower bound on the return value comes from the fact that each number is an unbiased estimate of the MAD of the list. So if all input numbers have equal probability, then they should be very close to the true MAD.
2. Null values in input are treated as 0's and do not affect the final result. This could be considered a precondition, but it would be better to make this part of the postcondition since it is an implementation detail.
3. If there are multiple nulls or infs then the return value is not well defined (and that may be useful information). Maybe we should consider the possibility of returning None rather than a number? This could also be considered as an invariant, but it would be less important than the first condition. 

So maybe postcondition 1 is "return value non-null iff input list contains no nulls or infs". This makes the return value depend on the whole function (as opposed to a single local variable), which might make things clearer than if it were just asserted in a way that doesn't really express this. It also might be a bit of a stretch, since the result isn't a number and is therefore not a value that would otherwise be part of the invariants in the function. But maybe