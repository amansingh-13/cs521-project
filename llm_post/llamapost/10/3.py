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
When you are satisfied with your postcondition, paste it into the box below.

You may make any assumptions about what the variables contain that you deem reasonable and necessary to achieve a correct answer for your postcondition. You may not assume knowledge of the implementation details (including the function being implemented) of make_palindrome. If necessary, explain why you are making such an assumption with a comment above the assert statement in your postcondition.
"""
def is_palindrome(string):
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string):
    """ Find the shortest palindrome that begins with string """
    # If it's already a palindrome, just return it.
    if is_palindrome(string):
        return string
    
    # Keep adding characters to the front of the string until it becomes a palindrome.
    while not is_palindrome(string):
        string += string[0]
        
    return string

def postcondition():
    """ If the postcondition calls any functions external to the program context, they should only be those from the functional subset of python. """
    assert make_palindrome("") == "", "make_palindrome(\"\") should return \"\"."
    # make_palindrome("") returns "" even though it doesn't start with an empty string.
    assert make_palindrome("a") == "a", "make_palindrome(\"a\") should return \"a\"."
    # This assertion fails because we add the front character to the back.
    assert make_palindrome("aa") ==