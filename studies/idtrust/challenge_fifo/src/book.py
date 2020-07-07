from fifo import FifoString
from operations import Operations


class Book:
    __slots__ = ['__queue', '__operations', '__number_of_operations', '__can_add_operation']

    def __init__(self, operations: Operations, number_of_operations: int = 1):
        self.__queue = FifoString()
        self.__operations = operations
        self.__number_of_operations = self.__valid_operations_number(number_of_operations)
        self.__can_add_operation = True

    @property
    def can_add_operation(self):
        return self.__can_add_operation

    def add_operation(self, operation: str) -> None:
        if self.__number_of_operations is not 0:
            self.__queue.enqueue(operation)
            self.__decrease_number_of_operations()
        else:
            raise ValueError('Exceeded number of operations allowed.')

    def __decrease_number_of_operations(self):
        self.__number_of_operations -= 1
        if self.__number_of_operations == 0:
            self.__can_add_operation = False

    def execute(self) -> int:
        return self.__operations.execute(self.__queue.dequeue())

    @staticmethod
    def __valid_operations_number(operations_number) -> int:
        if operations_number < 1 or operations_number > 100000:
            raise ValueError("The operations number doesn't can less than 1 or greater than 1000000000.")
        else:
            return operations_number
