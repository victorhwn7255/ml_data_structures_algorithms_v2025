pick = 73

def guess(num: int) -> int:
    """
    Simulates the LeetCode guess API.

    Returns:
        -1 if num > pick   → your guess is too high
         1 if num < pick   → your guess is too low
         0 if num == pick  → correct guess
    """
    if num > pick:
        return -1
    elif num < pick:
        return 1
    else:
        return 0