import warnings


def check_if_fruit(fruit: str) -> bool:
    if fruit == "tomato":
        warnings.warn("It's also a veggie!", ThisFruitIsAlsoAVeggie)
    return True


class ThisFruitIsAlsoAVeggie(Warning): ...
