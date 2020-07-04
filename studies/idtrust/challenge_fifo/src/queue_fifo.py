from node import Node


class Queue:
    __slots__ = ['__begin', '__last', '__length']

    def __init__(self):
        self.__begin = None
        self.__last = None
        self.__length = 0

    def enqueue(self, number: int):
        new = Node(number)
        if self.__begin is None:
            self.__begin = new
        elif self.__last is not None:
            self.__last.after = new
        self.__last = new
        self.__increment_size()

    def dequeue(self) -> int:
        first = self.__begin
        self.__begin = first.after
        self.__decrement_size()
        return first.value

    def print(self):
        return self.__begin.value

    @property
    def length(self) -> int:
        return self.__length

    def __increment_size(self):
        self.__length += 1

    def __decrement_size(self):
        self.__length -= 1
