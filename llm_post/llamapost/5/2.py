You have the following code context, function stub and natural language specification (in the form of a code comment) for intersperse. When implemented, the function should comply with this natural language specification:
from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers'
    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """

Write a symbolic postcondition for intersperse consisting of exactly one assert statement. For variables, use only the function input parameters and a hypothetical return value, which we'll assume is stored in a variable return_val. If the postcondition calls any functions external to the program context, they should only be those from the functional subset of python. Although the postcondition should be less complex than the function itself, it should not be trivial. It should encapsulate an aspect of the function without implementing the function. The format of your response should be:
```CODE FOR EXACTLY ONE POSTCONDITION WITH ASSERT HERE```

Intersperse takes two inputs and returns one result. Write three assert statements that test these three cases for intersperse with the values 4, [1, 2, 3], and 0. The format of your response should be:
```CODE FOR THREE ASSERTS HERE```

Consider the function that removes duplicates from a list of integers:
from typing import List

def dedup(nums: List[int]) -> List[int]:
    """ Remove all duplicate elements from `nums'
    >>> dedup([1, 2, 3])
    [1, 2, 3]
    >>> dedup([1, 1, 3])
    [1, 3]
    >>> dedup([3, 2, 1])
    [3, 2, 1]
    """
    result: List[int] = []
    for i in nums:
        if not result or i != result[-1]:
            result.append(i)
    return result

You may use this function in your tests to ensure that dedup does what it's supposed to do. To do so, you need to include it at the top of your file like you did with dedup and import it just as you have import assert not assert. Use `assert dedup([1, 1, 3]) == [1, 3]` to test the case where all the duplicates are removed. Write a second assertion testing the case where there is only one duplicate in the list of integers ([1, 1, 3]). Finally, write a third assertion that tests the case where there are no duplicated elements in the list (dedup([3, 2,