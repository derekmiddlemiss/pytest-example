import random
from typing import TypeVar

T = TypeVar("T")


def fetch_from_source() -> list[str]:
    # pretend that this function fetches from external source
    choices = ['a', 'b', 'c', 'd', 'e', 'f']
    return random.choices(choices, k=4)

