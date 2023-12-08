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

Write a natural language specification for make_palindrome that describes one aspect of this postcondition. For variables, use only the function input parameters and a hypothetical return value, which we'll assume is stored in a variable return_val. The format should be:
```DESCRIPTION OF EXACTLY ONE POSTCONDITION HERE```

If your code has any errors, please specify those (and the correct way to fix them) in response. Your postcondition and description should be as clear and complete as possible; they should not contain errors of any kind.

Here's an example of a natural language specification of a postcondition:
```
The postcondition states that when given a string s, the function returns the string s iff it is already a palindrome or the reversed version of the input string iff it is not a palindrome. Thus, the returned value is always either s iff s is already a palindrome or s_rev iff s is not already a palindrome, where s_rev is the reversed form of s (with its letters in reverse order).
```
Here's an example of an actual postcondition:
```
return_val == s if s == s[::-1] else return_val == s[::-1] 
```
The postcondition states that when given a string s, the function returns the same value as its input (the original string) when the original string is a palindrome or the reversed version of the original string otherwise. Thus, the returned value is always either the original string iff it is already a palindrome or the reversed form of the input string iff it is not already a palindrome.
"""

