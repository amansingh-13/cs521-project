To solve this problem, we can use the concept of relative velocity. Since all cars are moving at the same speed, we can imagine that the left-moving cars are stationary or the right-moving cars are moving at twice the speed in the opposite direction. 

Now, for each right-moving car, we need to check how many left-moving cars are in front of it. The number of collisions for each right-moving car will be equal to the number of left-moving cars in front of it.

To implement this logic, we can use a nested loop. The outer loop will iterate over the right-moving cars, or the inner loop will iterate over the left-moving cars. We can use a counter variable to keep track of the number of collisions.

Here's the implementation:

def car_race_collision(n: int) -> int:
    collisions = 0
    for i in range(n):
        for j in range(i+1, n):
            collisions += 1
    return collisions

This implementation has a time complexity of O(n^2), as we are checking for collisions between all pairs of cars.