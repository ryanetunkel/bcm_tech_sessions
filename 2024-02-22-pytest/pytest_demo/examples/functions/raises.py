from dataclasses import dataclass

def check_if_more_than_42(number: int):
   if number > 42:
       raise ValueError("Must be 42 or less!")

def check_if_its_exactly_100(number: int):
    """ Example with custom exception """
    if number == 100:
        raise CannotBeExactly100

@dataclass
class CannotBeExactly100(Exception):
    msg = "Number cannot be exactly 100."
