You have the following code context, function stub and natural language specification (in the form of a code comment) for all_prefixes. When implemented, the function should comply with this natural language specification:
from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """

Write a symbolic postcondition for all_prefixes consisting of exactly one assert statement. For variables, use only the function input parameters and a hypothetical return value, which we'll assume is stored in a variable return_val. If the postcondition calls any functions external to the program context, they should only be those from the functional subset of python. Although the postcondition should be less complex than the function itself, it should not be trivial. It should encapsulate an aspect of the function without implementing the function. The format of your response should be:
```CODE FOR EXACTLY ONE POSTCONDITION WITH ASSERT HERE```
**HINT: Be sure to check that you're using a variable for the return value and that you're using variables instead of literal values in the assert statement.**


#### The answer is 
```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    return_val = ['']
    for i in range(len(string)):
        a = len(return_val)
        temp = []
        for j in range(a):
            temp.append(string[0:j+1])
            
        return_val += temp
        
    return return_val
```

###### 3. Implement the function is_palindrome(x) from exercise 2 using symbolic postconditions.

You have the following code context,