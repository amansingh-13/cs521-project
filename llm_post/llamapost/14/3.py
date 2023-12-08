You have the following code context, function stub and natural language specification (in the form of a code comment) for all_prefixes. When implemented, the function should comply with this natural language specification:
from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """

Write a symbolic postcondition for all_prefixes consisting of exactly one assert statement. For variables, use only the function input parameters and a hypothetical return value, which we'll assume is stored in a variable return_val. If the postcondition calls any functions external to the program context, they should only be those from the functional subset of python. Although the postcondition should be less complex than the function itself, it should not be trivial. It should encapsulate an aspect of the function without implementing the function. The format of your response should be:
```CODE FOR EXACTLY ONE POSTCONDITION WITH ASSERT HERE```


Note that the solution to this exercise does not require any loops, recursion or string operations other than indexing and slicing. In addition, a general strategy for solving such exercises is to write your own test cases to guide you toward a correct implementation.

### Solution
```python
def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string

    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    return [string[:i] for i in range(len(string)+1)]
```
![image](https://user-images.githubusercontent.com/87369418/142054334-f9a57b2d-dbee-486d-87bd-5c369621947d.png)
### Testing code
```python
print(all_prefixes('abc'))
```
### Output 
```python
['a', 'ab', 'abc']
```
### Natural Language Specification
The output of all_prefixes should be a list containing the following prefixes for any input string.
```python
Input: 'abc'
output = ['a', 'ab', 'abc']
```
![image](https://user-images.githubusercontent.com/87369418/142058218-bccb52d5-cbf0-4fbe-8b58-f42e5a88ed96.png)
##