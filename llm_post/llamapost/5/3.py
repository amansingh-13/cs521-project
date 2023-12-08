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

### Exercises 4-10 through 4-28

Complete each exercise, using only the Python and functions you have learned about in this section. Test your solutions against the provided test cases (in the form of a main function) to ensure they are correct. If you are unsure how to solve any of these exercises, get help from your mentors or submit to https://classroom.github.com/a/L9GgZHXd

[Exercises 4-10](/src/chap_exercise_4_10.py)
```PYTHON
def remove_last(L): # list L, removing last element
    del L[-1]      # [22, 23, 24], list.remove(x: int), where x is a member of the list
    return L

print(list(range(0, 5)))
[0, 1, 2, 3, 4]

remove_last([0, 1, 2, 3, 4])
[0, 1, 2, 3]
```

[Exercises 4-11](/src/chap_exercise_4_11.py)

```PYTHON
L = ['a', 'b', 'c']
del L[1:3]      # [0, 2, 3], list.remove(x: int), where x is a member of the list
print(L)
['a', 'c']
```

[Exercises 4-12](/src/chap_exercise_4_1