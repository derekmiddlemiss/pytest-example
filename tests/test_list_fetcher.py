from src.list_fetcher import fetch_first
from pytest import raises, fixture


@fixture()
def my_list():
    return [1, 2, 3, 4, 5]


@fixture()
def empty_list():
    return []


def test_list_fetcher(my_list):
    assert fetch_first(my_list) == 1


def test_list_fetcher_empty(empty_list):
    with raises(IndexError):
        fetch_first(empty_list)


