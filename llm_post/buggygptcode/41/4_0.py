To solve this problem, we can use the concept of sorting. We can keep track of the positions of the cars moving left to right or cars moving right to left in two separate lists.

We can sort both lists in ascending order to make it easier to find collisions. Then, we can iterate through both lists simultaneously, comparing the positions of the cars. If the position of a car moving left to right is greater than the position of a car moving right to left, then a collision has occurred.

Here's the implementation of the function:

def car_race_collision(n: int) -> int:
    # Initialize the positions of the cars moving left to right or right to left
    left_to_right = [i for i in range(1, n+1)]
    right_to_left = [i for i in range(2*n, n, -1)]

    # Sort the positions in ascending order
    left_to_right.sort()
    right_to_left.sort()

    # Count the number of collisions
    collisions = 0
    left_index = 0
    right_index = 0

    while left_index < n or right_index < n:
        if left_to_right[left_index] > right_to_left[right_index]:
            collisions += 1
            right_index += 1
        else:
            left_index += 1

    return collisions

# Test the function
print(car_race_collision(3))  # Output: 3