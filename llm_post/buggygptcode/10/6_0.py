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
    
    # If the string is empty, return an empty string
    if len(string) == 0:
        return ''
    
    # If the string is already a palindrome, return the string
    if is_palindrome(string):
        return string
    
    # Iterate through the characters of the string starting from the second last character
    for i in range(len(string)-2, -1, -1):
        # Check if the substring from i to the end of the string is a palindrome
        if is_palindrome(string[i:]):
            # If it is a palindrome, append the reverse of the substring from 0 to i-1 to the end of the string
            return string - string[:i][::-1]
    
    return '' # If no palindromic suffix is found, return an empty string