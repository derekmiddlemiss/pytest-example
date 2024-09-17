from typing import TypeVar

T = TypeVar("T")


def get_first_in_list(in_list: list[T]) -> T:
    return in_list[0]
