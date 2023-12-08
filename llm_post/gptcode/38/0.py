To implement the `decode_cyclic` function, we need to reverse the steps taken in the `encode_cyclic` function. Specifically, we need to:
1. Split the encoded string into groups of three characters.
2. Reverse the cyclic rotation of each group.
3. Join the groups together to form the decoded string.

Here's the implementation of the `decode_cyclic` function:

```python
def decode_cyclic(s: str) -> str:
    # Split string into groups of three characters
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    
    # Reverse the cyclic rotation of each group
    groups = [(group[-1] + group[:-1]) if len(group) == 3 else group for group in groups]
    
    # Join the groups together to form the decoded string
    return "".join(groups)
```

Now you can use both `encode_cyclic` and `decode_cyclic` functions to encode and decode strings using cyclic rotations.