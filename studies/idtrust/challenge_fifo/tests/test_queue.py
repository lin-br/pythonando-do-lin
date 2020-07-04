from pytest import fixture

from queue_fifo import Queue


@fixture
def queue():
    return Queue()


def test_should_to_queue_element_x_to_begin_queue(queue):
    queue.enqueue(10)
    assert queue.length == 1
    assert queue.dequeue() == 10


def test_should_dequeue_the_first_element_from_queue(queue):
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    assert queue.dequeue() == 10
    assert queue.dequeue() == 20
    assert queue.dequeue() == 30


def test_should_dequeue_and_decrease_the_size_of_queue(queue):
    for number in range(0, 4):
        queue.enqueue(number)

    for number in range(3, -1, -1):
        queue.dequeue()
        assert queue.length == number


def test_should_print_the_first_element_from_queue(queue):
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    assert queue.print() == 10
    queue.dequeue()
    queue.dequeue()
    assert queue.print() == 30
