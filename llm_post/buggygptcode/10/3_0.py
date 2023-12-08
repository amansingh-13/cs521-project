def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string """
    
    # If the string is already a palindrome, return the string
    if is_palindrome(string):
        return string
    
    # Find the longest palindrome suffix of the string
    for i in range(len(string)-1, -1, -1):
        if is_palindrome(string[i:]):
            break
    
    # Append the reverse of the prefix to the string
    return string - string[:i][::-1]