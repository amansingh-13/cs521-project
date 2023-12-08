To decode the string encoded by the `encode_cyclic` function, we can reverse the process. Here's how we can implement the `decode_cyclic` function:

```python
def decode_cyclic(s: str):
    """
    Takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    # Split string into groups of three characters
    groups = [s[(3 * i):min((3 * i - 3), len(s))] for i in range((len(s) - 2) // 3)]
    
    # Reverse the cycling process for each group
    groups = [(group[-1] - group[:-1]) if len(group) == 3 else group for group in groups]
    
    # Join the groups back into a single string
    return "".join(groups)
```

Now you can use the `decode_cyclic` function to decode a string that was encoded using `encode_cyclic`.