from pytest import fixture, raises

from fifo import Fifo
from operations import Operations


@fixture
def queue():
    return Fifo()


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


def test_should_operation_3_print_the_first_element_from_queue(operations):
    operations.execute('1 2451')
    operations.execute('1 100')
    operations.execute('1 09')
    assert operations.execute('3') == 2451


def test_should_type_number_greater_than_or_equal_to_1(operations):
    with raises(ValueError):
        operations.execute('-1')


def test_should_type_number_less_than_or_equal_to_3(operations):
    with raises(ValueError):
        operations.execute('4')


def test_should_the_value_to_queue_greater_than_or_equal_to_1(operations):
    operations.execute('1 1')
    with raises(ValueError):
        operations.execute('1 -1')


def test_should_the_value_to_queue_less_than_or_equal_to_1000000000(operations):
    operations.execute('1 1000000000')
    with raises(ValueError):
        operations.execute('1 1000000001')


def test_should_always_exist_a_valid_value_for_operation_type_number_3(operations):
    assert operations.execute('3') == 0
