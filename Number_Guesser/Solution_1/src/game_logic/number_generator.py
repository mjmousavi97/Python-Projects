import random
def generat_random_number(start: int, end: int) -> int:
    """
    Generates and returns a random integer between 'start' and 'end' (inclusive).

    :Parameters:
    start (int): The minimum value in the range (inclusive).
    end (int): The maximum value in the range (inclusive).

    :Returns:
    int: A random integer within the specified range [start, end].

    This function uses Python's random.randint to generate the number.
    """
    return random.randint(start, end)