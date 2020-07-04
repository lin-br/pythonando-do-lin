from pytest import fixture

from operations import Operations
from queue_fifo import Queue


@fixture
def queue():
    return Queue()


@fixture
def operations(queue):
    return Operations(queue)


def test_should_operation_1_to_queue_element_x_to_begin_queue(operations, queue):
    operations.execute('1 10')
    assert queue.length == 1


def test_should_operation_2_dequeue_the_first_element_from_queue(operations, queue):
    operations.execute('1 10')
    operations.execute('1 20')
    operations.execute('1 30')
    operations.execute('2')
    assert queue.length == 2


def test_should_operation_3_print_the_first_element_from_queue():
    pass


def test_should_type_number_greater_than_or_equal_to_1():
    pass


def test_should_type_number_less_than_or_equal_to_3():
    pass


def test_should_the_value_to_queue_greater_than_or_equal_to_1():
    pass


def test_should_the_value_to_queue_less_than_or_equal_to_1000000000():
    pass


def test_should_always_exist_a_valid_value_for_operation_type_number_3():
    pass
