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


### Questions for discussion during office hours
Please share these questions with your office hour buddies so we can go over them together! You don't have to do all of these - but I encourage you to at least start working on as many as you can.

1.  Explain the difference between a property and a postcondition?
2.  What are two of each type of testing: unit, integration, system and property-based?
3.  Are there any other types of testing that you should be aware of? If so, what are they?
4.  Why is property-based testing important (in your experience)?
5.  Is property-based testing a "must have" or a "nice to have"?
6.  What do you think about the idea that code should be tested according to its properties, rather than how it happens to behave at the moment? In other words, what are some of the drawbacks/downsides of testing according to behavior?
7.  Why might property-based testing actually be more valuable than normal unit tests in a software suite? Explain your answer with an example.
8.  What do you think about test doubles (fake objects, mocks etc)? What are two things that may or may not help when using them?
9.  Why might we want to be careful when choosing our "assertion" libraries? If it's important for me to use a certain library over another one, why is that?
10. Are there any other testing-related concepts you think are worth knowing about in the world of software engineering?
11. What tools have been useful to your team during your experience with TDD and BDD? Please name at least two.

### 📝 Learning objectives