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
Note that to use assert you may need to import AssertionError as well (see below). 

### Solution - Postcondition with a single assert statement for make_palindrome function
```Python
def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]


def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string.
    Algorithm idea is simple:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string an appropriate character. This may mean deleting or adding a character to the original string. The appropriate character will be determined by comparing the length of the returned suffix and the return value of the is_palindrome function (with respect to the appended string). If the returned suffix is shorter than the palindrome, then a character must have been added in order for the string to end up being a palindrome. Therefore, we delete the last letter from the original string in order to make it a palindrome. If it is longer than the palindrome, then that means the palindrome has been created by appending an extra character to the suffix. In this case, we add one less of the returned suffix in order to create the desired result, which is a palindrome.
    """
    return_val = ""
    if len(string) == 0:
        return_val = string
    else:
        max_suffix = find_longest_palindrome(string[1:])
        if