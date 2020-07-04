class Operations:
    __slots__ = ['__queue']

    def __init__(self, queue):
        self.__queue = queue

    def execute(self, operation: str):
        if operation.startswith('1'):
            self.__queue.enqueue(int(operation.split(' ')[1]))
