To implement the `decode_cyclic` function, we need to reverse the steps performed in the `encode_cyclic` function. Here's the implementation:

```python
def decode_cyclic(s: str):
    # split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # reverse the cycle for each group. Unless group has fewer elements than 3.
    groups = [(group[-1] + group[:-1]) if len(group) == 3 else group for group in groups]
    return "".join(groups)
```

This function splits the encoded string into groups of three characters or reverses the cycle of elements in each group (except for groups with fewer than 3 elements). Finally, it joins the groups together to form the decoded string.