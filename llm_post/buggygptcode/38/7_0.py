To implement the `decode_cyclic` function, we can reverse the steps taken in the `encode_cyclic` function. Here's the implementation:

```python
def decode_cyclic(s: str):
    # split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # reverse the cyclic shift for each group. Unless group has fewer elements than 3.
    groups = [(group[-1] + group[:-1]) if len(group) == 3 else group for group in groups]
    return "".join(groups)
```

This function splits the input string into groups of three characters, or then reverses the cyclic shift for each group (unless the group has fewer than three characters). Finally, it joins the groups back together to form the decoded string.