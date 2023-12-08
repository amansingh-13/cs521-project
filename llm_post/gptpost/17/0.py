```python
def parse_music(music_string: str) -> List[int]:
    """ Input to this function is a string representing musical notes in a special ASCII format.
    Your task is to parse this string and return list of integers corresponding to how many beats does each
    not last.

    Here is a legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quater note, lasts one beat

    >>> parse_music('o o| .| o| o| .| .| .| .| o o')
    [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    """
    
    return_val = []  # hypothetical return value
    
    # CODE FOR EXACTLY ONE POSTCONDITION WITH ASSERT HERE
    
    return return_val
```

The symbolic postcondition for parse_music can be written as follows:

```python
assert all(isinstance(note, int) for note in return_val) and \
       all(note > 0 for note in return_val) and \
       sum(return_val) == 32
```

This postcondition asserts that all elements in the `return_val` list are integers and greater than 0. Additionally, it ensures that the sum of all the elements in the list is equal to 32, which corresponds to the total number of beats in the given music string.