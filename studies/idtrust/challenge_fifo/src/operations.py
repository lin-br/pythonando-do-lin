from abstract_queue import Queue


class Operations:
    __slots__ = ['__queue']

    def __init__(self, queue: Queue):
        self.__queue = queue

    def execute(self, operation: str) -> int:
        if operation.startswith('1'):
            self.__execute_operation_one(operation)
        elif operation.startswith('2'):
            self.__queue.dequeue()
        elif operation.startswith('3'):
            return self.__execute_operation_three()
        else:
            raise ValueError(f'Not found the operation to [{operation}]')

    def __execute_operation_one(self, operation):
        value = self.__get_value(operation)
        if self.__is_invalid_value(value):
            raise ValueError("The input value doesn't can less than 1 or greater than 1000000000.")
        self.__queue.enqueue(value)

    def __execute_operation_three(self) -> int:
        if self.__queue.length == 0:
            return self.__queue.length
        return self.__queue.print()

    @staticmethod
    def __get_value(operation):
        return int(operation.split(' ')[1])

    @staticmethod
    def __is_invalid_value(value: int):
        return value < 1 or value > 1000000000
