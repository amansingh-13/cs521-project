You have the following code context, function stub and natural language specification (in the form of a code comment) for has_close_elements. When implemented, the function should comply with this natural language specification:
from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """

Write a symbolic postcondition for has_close_elements consisting of exactly one assert statement. For variables, use only the function input parameters and a hypothetical return value, which we'll assume is stored in a variable return_val. If the postcondition calls any functions external to the program context, they should only be those from the functional subset of python. Although the postcondition should be less complex than the function itself, it should not be trivial. It should encapsulate an aspect of the function without implementing the function. The format of your response should be:
```CODE FOR EXACTLY ONE POSTCONDITION WITH ASSERT HERE```
The first line should just be the word "CODE", with a colon after it, and all subsequent lines of your response should be indented as if they are contained in that block. It's okay to use multiple lines for long postconditions. The comment block will be evaluated by our testing script, but it will not affect the final grade unless you also make changes to the function itself.

[Previous](./ch1-fake-tests) | [Next](./ch3-postcondition-example)

### References:

* [Natural Language Specification 1](https://en.wikipedia.org/wiki/Natural_language_specification)
* [Natural Language Specification 2