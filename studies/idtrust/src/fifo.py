from abc import ABC, abstractmethod


class Fifo(ABC):

    @abstractmethod
    def to_queue(self, x: int):
        pass

    @abstractmethod
    def dequeue(self) -> int:
        pass


class Node:
    __slots__ = ['__value', '__next']

    def __init__(self, value: int):
        self.__value = value
        self.__next = None

    def connect(self, connect_next):
        self.__next = connect_next

    def disconnect(self):
        del self.__next

    @property
    def value(self):
        return self.__value


class Ops(Fifo):
    __slots__ = ['__begin', '__end', '__length']

    def __init__(self):
        self.__begin = None
        self.__end = None
        self.__length = 0

    def to_queue(self, op: int):
        if self.__begin is None:
            self.__begin = Node(op)
        if self.__end is None:
            self.__end = Node(op)
        self.__end.connect(Node(op))
        self.__length += 1

    def dequeue(self) -> int:
        result = self.__begin
