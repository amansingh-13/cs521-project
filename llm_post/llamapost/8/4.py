You have the following code context, function stub and natural language specification (in the form of a code comment) for sum_product. When implemented, the function should comply with this natural language specification:
from typing import List, Tuple


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    """

Write a symbolic postcondition for sum_product consisting of exactly one assert statement. For variables, use only the function input parameters and a hypothetical return value, which we'll assume is stored in a variable return_val. If the postcondition calls any functions external to the program context, they should only be those from the functional subset of python. Although the postcondition should be less complex than the function itself, it should not be trivial. It should encapsulate an aspect of the function without implementing the function. The format of your response should be:
```CODE FOR EXACTLY ONE POSTCONDITION WITH ASSERT HERE```
Then, write a specification (without any code) that ensures the postcondition for sum_product. It should include only the natural language specification and no assert statements. If you have trouble with this step, please ask your TA or TSI for help.
```CODE FOR SPECIFICATION WITHOUT ASSERT HERE```
When testing, write a test that calls your function sum_product in some way that exercises the postcondition. Be sure to test it both with and without input values. Your specification must be correct before you'll get full credit for this task. You may also receive partial credit if you include the postcondition in the implementation but fail to specify it in your test.
```CODE FOR TEST THAT EXERCISES POSTCONDITION HERE```
To test your assertion, you should either:
1) write a function that returns True iff the postcondition holds (passes the test) for all possible inputs and call it from your test, or
2) modify sum_product to include a method that asserts the specification. This way, you can run your tests and confirm that they pass before proceeding with the next step. You may receive partial credit if the first assertion fails but not the second.
```CODE FOR FUNCTION THAT ASSERTS SPECIFICATION HERE```
Once you've confirmed that your specification ensures the postcondition, add it to sum_product in three ways (but do one of them):
1) Replace your test with a test that asserts the specification rather than calling sum_product directly.
2) Add a method assert_specification() within sum_product that asserts the specification. Call this method from your test.
3) Write a postcondition for sum_