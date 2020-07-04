from pytest import fixture

from queue_fifo import Queue


@fixture
def queue():
    return Queue()


def test_should_to_queue_element_x_to_begin_queue(queue):
    queue.to_queue(10)
    assert queue.length == 1
    assert queue.dequeue() == 10


def test_should_dequeue_the_first_element_from_queue(queue):
    queue.to_queue(10)
    queue.to_queue(20)
    queue.to_queue(30)
    assert queue.dequeue() == 10
    assert queue.dequeue() == 20
    assert queue.dequeue() == 30


def test_should_dequeue_and_decrease_the_size_of_queue(queue):
    for number in range(0, 4):
        queue.to_queue(number)

    for number in range(3, -1, -1):
        queue.dequeue()
        assert queue.length == number


def test_should_print_the_first_element_from_queue():
    pass


def test_should_the_number_of_operations_greater_than_or_equal_to_1():
    pass


def test_should_the_number_of_operations_less_than_or_equal_to_100000():
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
