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

# Initial Thoughts
- I want to do this using recursion, and not for loops.
- I will need a stack of parens as I traverse the string.

# Steps

### Write an empty function header
```python
def separate_paren_groups(paren_string: str) -> List[str]:
```
### Initialize list to hold answer and add it to return value (see below for postcondition.)
```python
    # We'll be returning this. If we just return the answer, we are not using recursion
    # as we should.
    return_val = []
    # Initializing a stack. 0 is empty paren, 1 is open paren.
    stack = []
```
### Iterate over string and build list from it
- If the current character is not an opening bracket, append it to the
answer. Otherwise, push the opening bracket on the stack.
- After each iteration, check if the top of the stack has a matching closing paren
to the opening paren we just encountered.
- If so, pop the top off the stack and continue iterating over string.
- If not, add the character to the answer and start looking for a match.
```python
    # Looping through characters in the string
    for c in paren_string:
        # If not an open bracket, append it to the answer list.
        if c != '(':
            return_val += c
        else:
            stack.append(c)
        
        # Check if we have a matching bracket to pop off the stack.
        # Note that top of stack will always be open paren, as we are iterating over the string.