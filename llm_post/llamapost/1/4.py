You have the following code context, function stub and natural language specification (in the form of a code comment) for separate_paren_groups. When implemented, the function should comply with this natural language specification:
from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

Write a symbolic postcondition for separate_paren_groups consisting of exactly one assert statement. For variables, use only the function input parameters and a hypothetical return value, which we'll assume is stored in a variable return_val. If the postcondition calls any functions external to the program context, they should only be those from the functional subset of python. Although the postcondition should be less complex than the function itself, it should not be trivial. It should encapsulate an aspect of the function without implementing the function. The format of your response should be:
```CODE FOR EXACTLY ONE POSTCONDITION WITH ASSERT HERE```

### Task 2: Write a unit test for separate_paren_groups
Write a unit test which confirms that the postcondition holds true by proving that return_val is indeed one of the values in your list result. Your unit test should not be trivial and should not use any functions from the functional subset of python.
```CODE FOR YOUR TEST HERE```
### Task 3: Implement separate_paren_groups
Write the function that meets your postcondition and makes the assertion you proved in your unit test to pass. In particular, your implementation should meet the following properties:
- Your solution is an iterative approach (no recursion)
- A balanced parentheses string will produce a list of balanced parentheses strings with correct paren count
- All balanced pairs of parentheses are included in the output list and no redundant groups are generated
- Any whitespace characters in the input will be removed from the output strings
- Any redundant whitespace is stripped from the input before processing it (including the last character which may be whitespace) to preserve parity
- The algorithm must run in linear time, meaning that it has O(N) runtime where N = len(s). You should not use any built-in Python methods for generating Fibonacci numbers or factorials since those take quadratic time.
```CODE FOR YOUR IMPLEMENTATION HERE```
### Task 4: Implement multiple tests to confirm that your solution meets the postcondition and has linear runtime
To confirm that the implementation is correct, implement a unit test for the following examples, as well as some random strings in which you feel your algorithm should hold true:
- Empty string
- Single characters (including parens)
- Pairs of matching parentheses
- Triplets of matching parentheses
- Qu