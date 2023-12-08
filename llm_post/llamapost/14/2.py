You have the following code context, function stub and natural language specification (in the form of a code comment) for all_prefixes. When implemented, the function should comply with this natural language specification:
from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """

Write a symbolic postcondition for all_prefixes consisting of exactly one assert statement. For variables, use only the function input parameters and a hypothetical return value, which we'll assume is stored in a variable return_val. If the postcondition calls any functions external to the program context, they should only be those from the functional subset of python. Although the postcondition should be less complex than the function itself, it should not be trivial. It should encapsulate an aspect of the function without implementing the function. The format of your response should be:
```CODE FOR EXACTLY ONE POSTCONDITION WITH ASSERT HERE```
If you are including multiple postconditions, please include all the relevant ones.

---
# Solution
* Postcondition: ```len(return_val) == len(string)+1-all([i in string for i in return_val]) or 0```

* Explanation: 
    * The assert statement should compare the list created by all_prefixes with the expected output.  
    * This postcondition compares the length of the list with the number of prefixes in the given word plus a 1-based counter to make sure there is only one prefix that was not seen, and it is the longest possible.  
    * To make this postcondition more efficient, we'll add an extra condition to check if any prefix in the returned list is included in the input string. If so, then all of the remaining prefixes are valid and have been counted correctly.  In that case, the postcondition will return True.  
    * To make this work, we'll create a list with all of the prefixes using a for loop over range(1, len(string)+1), then remove any prefix found in the input string to account for duplicates.
        * Since we are looping over every character 0-len(string) inclusive for prefixes