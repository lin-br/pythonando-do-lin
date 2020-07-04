from abstract_queue import Queue
from node import Node


class Fifo(Queue[int]):
    __slots__ = ['__begin', '__last']

    def __init__(self):
        super().__init__()
        self.__begin = None
        self.__last = None

    def enqueue(self, number: int):
        new = Node(number)
        if self.__begin is None:
            self.__begin = new
        elif self.__last is not None:
            self.__last.after = new
        self.__last = new
        super()._increment_size()

    def dequeue(self) -> int:
        first = self.__begin
        self.__begin = first.after
        super()._decrement_size()
        return first.value

    def print(self) -> int:
        return self.__begin.value
