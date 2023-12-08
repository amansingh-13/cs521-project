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

    # Symbolic postcondition
    assert isinstance(return_val, list)
    assert all(isinstance(n, int) for n in return_val)
    assert len(return_val) == music_string.count('o') + music_string.count('o|') + music_string.count('.|')
    assert sum(return_val) == music_string.count('o') * 4 + music_string.count('o|') * 2 + music_string.count('.|')
```