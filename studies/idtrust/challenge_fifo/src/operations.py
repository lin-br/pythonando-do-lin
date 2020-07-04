from queue_fifo import Queue


class Operations:
    __slots__ = ['__queue']

    def __init__(self, queue: Queue):
        self.__queue = queue

    def execute(self, operation: str):
        if operation.startswith('1'):
            self.__queue.enqueue(int(operation.split(' ')[1]))
        elif operation.startswith('2'):
            self.__queue.dequeue()
