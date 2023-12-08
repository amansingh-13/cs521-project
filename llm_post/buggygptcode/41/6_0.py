def car_race_collision(n: int) -> int:
    """
    Calculate the number of collisions that occur between two sets of cars moving towards each other.

    Args:
    - n: The number of cars in each set

    Returns:
    - The number of collisions that occur
    """
    # Calculate the number of collisions using combinatorics
    return n * (n - 1) // 2