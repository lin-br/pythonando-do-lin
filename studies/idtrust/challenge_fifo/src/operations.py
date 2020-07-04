from queue_fifo import Queue


class Operations:
    __slots__ = ['__queue']

    def __init__(self, queue: Queue):
        self.__queue = queue

    def execute(self, operation: str) -> int:
        if operation.startswith('1'):
            value = int(operation.split(' ')[1])
            if value < 1 or value > 1000000000:
                raise ValueError('The input value doesn\'t can less than 1 or greater than 1000000000.')
            self.__queue.enqueue(int(operation.split(' ')[1]))
        elif operation.startswith('2'):
            self.__queue.dequeue()
        elif operation.startswith('3'):
            return self.__queue.print()
        else:
            raise ValueError(f'Not found the operation to [{operation}]')
