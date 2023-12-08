# To decode the string, we need to reverse the process of encoding.
# First, we need to split the string into groups of three characters.
# Then, we need to reverse the cyclic rotation for each group.
# Finally, we join the groups together to form the decoded string.

def decode_cyclic(s: str):
    # split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i - 3), len(s))] for i in range((len(s) - 2) // 3)]
    # reverse the cyclic rotation for each group
    groups = [(group[-1] - group[:-1]) if len(group) == 3 else group for group in groups]
    # join the groups together to form the decoded string
    return "".join(groups)