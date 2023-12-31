# Main Program
def solution(start, length):
    """Find the Checksum."""
    checksum = 0
    for i in range(length, 0, -1):
        checksum = checksum ^ (
            row_xor(start + i - 1) ^ row_xor(start - 1)
        )
        start = start + length
    return checksum


def row_xor(x):
    """Output xor for a range(0,x)."""
    """We use the fact that xor of range(0,x)
    can be calculated in constant time."""
    outcome = [x, 1, x + 1, 0]
    return outcome[x % 4]
