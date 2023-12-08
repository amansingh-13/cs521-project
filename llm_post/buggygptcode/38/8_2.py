To implement the `decode_cyclic` function, we need to reverse the steps performed in the `encode_cyclic` function. Here's one way to do it:

```python
def decode_cyclic(s: str):
    # split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i - 3), len(s))] for i in range((len(s) - 2) // 3)]
    # reverse the cycling of elements in each group. Unless group has fewer elements than 3.
    groups = [(group[-1] - group[:-1]) if len(group) == 3 else group for group in groups]
    return "".join(groups)
```

In this implementation, we reverse the cycling of elements in each group by moving the last character to the beginning of the group. If a group has fewer than 3 characters, we leave it unchanged. Finally, we join the groups together to form the decoded string.