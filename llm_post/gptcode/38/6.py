To decode a string encoded with the `encode_cyclic` function, we need to reverse the encoding process. 

Here's the implementation for `decode_cyclic`:

```python
def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    # split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # reverse the cyclic rotation for each group. Unless group has fewer elements than 3.
    groups = [(group[-1] + group[:-1]) if len(group) == 3 else group for group in groups]
    return "".join(groups)
```

This function splits the string into groups of three characters, just like in the `encode_cyclic` function. Then, for each group, it reverses the cyclic rotation by moving the last character to the front. Finally, it joins the groups together to form the decoded string.

You can now use the `decode_cyclic` function to decode a string encoded with `encode_cyclic`.