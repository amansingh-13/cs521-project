You have the following code context, function stub and natural language specification (in the form of a code comment) for all_prefixes. When implemented, the function should comply with this natural language specification:
from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """

Write a symbolic postcondition for all_prefixes consisting of exactly one assert statement. For variables, use only the function input parameters and a hypothetical return value, which we'll assume is stored in a variable return_val. If the postcondition calls any functions external to the program context, they should only be those from the functional subset of python. Although the postcondition should be less complex than the function itself, it should not be trivial. It should encapsulate an aspect of the function without implementing the function. The format of your response should be:
```CODE FOR EXACTLY ONE POSTCONDITION WITH ASSERT HERE```
The code is
```python
def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    return ["a", "ab", "abc"]
```
and your code response is:
```python
assert string == return_val + string[:-1]
```
The postcondition says that the input string is returned with one character dropped. If this were a function in a larger program, you would check that the result makes sense. In this case, all that needs to be done is to verify it by asserting it. The code for the postcondition only has a single line of code (no nested if statements), and the return_val variable will have the same type (string) as the string input parameter
Postconditions should always use assert statements. You can write multiple assertions in a single function, but they all need to be in a single assertion statement.
You may find this resource helpful: https://realpython.com/python-assert/.

3. You have written a function find_max that finds the largest value in a list of numbers. However, the code is not working because you cannot use for loops inside functions. Here is the code:
```py
def find_max(nums):
    max = nums[0]
    for i in range(1, len(nums)):
        if max < nums[i]:
            max = nums[i]
    return max
```
You will be provided with a list of numbers. You must return the largest value from that list, without using