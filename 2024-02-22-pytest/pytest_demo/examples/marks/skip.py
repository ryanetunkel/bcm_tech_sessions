import math
import sys


def exp2(x: int) -> int:
    """Return 2 raised to the power x."""
    # If 3.11 or later, we can use the math function
    if sys.version_info.major == 3 and sys.version_info.minor >= 11:
        return math.exp2(x)
    # Else do it ourselves
    return 2**x
