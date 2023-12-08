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

---
### Problem 2
Write a symbolic precondition and postcondition for every function in the provided file `student_functional.py`, which can be found on Canvas under 'Files to be uploaded by student'. You do not need to submit this file, but it will help you understand how our grading works should you fail a particular component of your assignment.

---
### Problem 3 (15 points)

Write a function which can find the median value in an array of integers. For this first pass, your function should only handle cases where the list size is odd and the list size is even. You may assume that all list elements are integers. Your function does not need to be recursive. Hint: you might be able to use a for loop on the sorted version of your array.
from typing import List
def median(lst: List[int]) -> int:
    """ Return the median value from an array of integers `lst'
    >>> median([1, 2]) # should be 1.5 if handled correctly
    1.5
    >>> median([2, 3, 4]) # should be 2.5 if handled correctly
    2.5
    """
    return None # TODO: Write a solution here

---
### Problem 4 (8 points)

Write the function `check_sum` that returns whether or not an array of integers has a value equal to its sum. You do not need to handle cases where the list size is even or odd - for this first pass, please just return True if any element in your list matches the array's sum and False otherwise.
from typing import List
def check_sum(lst: List[int]) -> bool:
    """ Return whether