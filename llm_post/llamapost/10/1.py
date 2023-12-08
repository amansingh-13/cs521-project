You have the following code context, function stub and natural language specification (in the form of a code comment) for make_palindrome. When implemented, the function should comply with this natural language specification:


def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]


def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string.
    Algorithm idea is simple:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    >>> make_palindrome('')
    ''
    >>> make_palindrome('cat')
    'catac'
    >>> make_palindrome('cata')
    'catac'
    """

Write a symbolic postcondition for make_palindrome consisting of exactly one assert statement. For variables, use only the function input parameters and a hypothetical return value, which we'll assume is stored in a variable return_val. If the postcondition calls any functions external to the program context, they should only be those from the functional subset of python. Although the postcondition should be less complex than the function itself, it should not be trivial. It should encapsulate an aspect of the function without implementing the function. The format of your response should be:
```CODE FOR EXACTLY ONE POSTCONDITION WITH ASSERT HERE```

In this example, we need to prove the following postcondition:
```assert make_palindrome('cata') == 'catac'```
In order for our assert statement to be correct, it needs to be in the form of ```assert f(x) == g(x)```. The ```f(x)``` should be your symbolic postcondition, and the ```g(x)``` is the output of ```make_palindrome('cata')```, which we can assume for this example to be a string. Thus, the final format will look like this:
```assert <symbolic-postcondition> == 'catac'```

The natural language specification (in our case, ```assert make_palindrome(x) == g(x)```) has been translated into the symbolic postcondition (in our case, ```assert f(x) == g(x)```). If you're still unsure about how exactly to translate the natural language specification and/or write the final code with correct syntax, please ask for help.

*Remember: you can't call any functions that are not in the functional subset of python (e.g. ```print()``` or ```input()```). Also remember that assertions cannot use variables that are defined outside of the program context. The only variables we have access to are *x*, which is an argument of our function, and ```make_palindrome(<some-argument>)```, which we'll assume is stored in a variable called ```return_val```.*
```python
def make_palindrome(word):
    """
    This function takes in a word as a string, and returns a palindrome by removing all spaces.
    Input