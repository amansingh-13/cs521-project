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
Do not change any other file or line of code. You may add comments if helpful, but it is not necessary.
If you have questions about this problem or want to run some tests, check out this repl: https://replit.com/@cs61bl/p2-SeparateParenGroupsTester#main.py
You can also test your postcondition with a simple main like that in main_simple.py, and run it to see if it passes or fails. It should pass.
When you are done responding to this question, submit the entire contents of that file (with a commit). The repl is yours to keep. If you don't want any more feedback on this problem after that submission, then you may leave out your answer for this question - but be sure to submit it so we can see what postcondition you