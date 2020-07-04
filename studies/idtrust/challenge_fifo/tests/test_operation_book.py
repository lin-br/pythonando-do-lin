from pytest import fixture, raises

from book import Book
from fifo import Fifo
from operations import Operations


@fixture
def book():
    return Book(Operations(Fifo()))


def test_should_the_number_of_operations_greater_than_or_equal_to_1(book):
    with raises(ValueError):
        book.execute_operations(-1)


def test_should_the_number_of_operations_less_than_or_equal_to_100000(book):
    with raises(ValueError):
        book.execute_operations(100001)
