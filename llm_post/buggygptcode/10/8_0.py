def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string """
    if string == "":
        return ""
    else:
        i = len(string) - 1
        while i > 0:
            if string[:i+1] == string[:i+1][::-1]:  # check if prefix is a palindrome
                return string + string[:i][::-1]  # append reverse of prefix to the end
            i -= 1
        return string + string[:-1][::-1]  # if no palindromic suffix found, append reverse of string excluding last character