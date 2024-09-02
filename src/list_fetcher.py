from typing import Any
from typing import TypeVar

T = TypeVar("T")


def fetch_first(in_list: list[T]) -> T:
    return in_list[0]


if __name__ == '__main__':
    my_list_strs = ['2', '1', '3', '10']
    my_list_ints = [1, 2, 3, 4, 5]
    print(type(my_list_strs))
    print(type(my_list_strs[0]))
    first_string = fetch_first(my_list_strs)
    first_int = fetch_first(my_list_ints)
    print(type(first_string))
    print(type(first_int))

    print(sorted(my_list_strs))
