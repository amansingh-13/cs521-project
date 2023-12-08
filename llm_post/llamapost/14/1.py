You have the following code context, function stub and natural language specification (in the form of a code comment) for all_prefixes. When implemented, the function should comply with this natural language specification:
from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """

Write a symbolic postcondition for all_prefixes consisting of exactly one assert statement. For variables, use only the function input parameters and a hypothetical return value, which we'll assume is stored in a variable return_val. If the postcondition calls any functions external to the program context, they should only be those from the functional subset of python. Although the postcondition should be less complex than the function itself, it should not be trivial. It should encapsulate an aspect of the function without implementing the function. The format of your response should be:
```CODE FOR EXACTLY ONE POSTCONDITION WITH ASSERT HERE```

You can use pytest to test your code. To install pytest, run `pip install -U pytest`. Pytest will find and execute tests that are in any file named conftest.py in the current or a parent directory of where you run pytest from, regardless of what's in the files.
```python
import pytest
from main import all_prefixes

def test_1():
    assert all_prefixes('abc') == ['a', 'ab', 'abc']

```
Run `pytest` to execute the tests and make sure you have a passing test (runs with exit code 0).


You also need an example of how the function is called in your main file. It must be written as though it were runnable - meaning that all variables should be created, including any used by the function. Also note the use of variable-type annotations and docstrings.
```python
if __name__ == '__main__':
    string = input('Enter a string: ') # you can hard-code your own string here to test the function
    print(all_prefixes(string))

```
In this file, add code for running your program from the command line that will pass the tests and print out the result. For example, if the user enters "abc" when prompted for a string, it should print `['a', 'ab', 'abc']`. You can use `input()` to accept input from the user at runtime or hard-code your own test-string as above.
```python
import sys
sys.path.insert(0, './')  # make sure we run main.py first so it gets loaded into memory.
from main import all