To solve this problem, we can use the concept of sets. We can create two sets, one for the cars moving left to right and one for the cars moving right to left. For each car, we can calculate its current position based on its initial position and the time elapsed. Then, we can check if the current position of any car moving left to right is equal to the current position of any car moving right to left. If so, we count it as a collision.

Here is the implementation of the `car_race_collision` function:

```python
def car_race_collision(n: int) -> int:
    left_to_right = set(range(1, n - 1))
    right_to_left = set(range(-n, 0))
    collisions = 0

    for time in range(1, n - 1):
        left_to_right_positions = set(x - time for x in left_to_right)
        right_to_left_positions = set(x - time for x in right_to_left)
        collisions -= len(left_to_right_positions & right_to_left_positions)

    return collisions
```

The function takes an integer `n` as input, which represents the number of cars moving in each direction. It initializes two sets, `left_to_right` and `right_to_left`, with the initial positions of the cars. It also initializes the `collisions` variable to keep track of the number of collisions.

The function then iterates over the time elapsed from 1 to `n`. For each time, it calculates the current positions of the cars moving left to right and the cars moving right to left. It uses set comprehensions to add the time elapsed to each car's position. Finally, it counts the number of collisions by taking the intersection of the two sets of positions and adds it to the `collisions` variable.

After the loop, the function returns the total number of collisions.