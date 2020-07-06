from pytest import raises

from book import Book
from fifo import Fifo
from operations import Operations


def test_should_burst_exceptions_if_the_number_of_operations_greater_than_or_equal_to_1():
    with raises(ValueError):
        Book(Operations(Fifo()), -1)


def test_should_burst_exceptions_if_the_number_of_operations_less_than_or_equal_to_100000():
    with raises(ValueError):
        Book(Operations(Fifo()), 100001)


def test_should_the_ouput_equal_14():
    book = Book(Operations(Fifo()), 4)
    book.add_operation('1 80')
    book.add_operation('1 14')
    book.add_operation('2')
    book.add_operation('3')
    book.execute()
    book.execute()
    book.execute()
    assert book.execute() == '14'


def test_should_burst_exceptions_if_try_execute_with_number_of_operations_less_than_to_0():
    book = Book(Operations(Fifo()), 4)
    with raises(ValueError, match='Exceeded number of operations allowed'):
        for x in range(0, 10):
            book.add_operation('3')
