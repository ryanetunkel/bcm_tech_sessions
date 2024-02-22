"""
Same code as warns.py

This addresses the bug in that code
"""

import warnings


def check_if_fruit(fruit: str) -> bool:
    # The bug is in here, where tomato is assumed to given all lowercase
    if fruit == "tomato":
        warnings.warn("It's also a veggie!", ThisFruitIsAlsoAVeggie)
    return True


class ThisFruitIsAlsoAVeggie(Warning): ...
