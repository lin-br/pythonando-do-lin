from abc import ABC, abstractmethod
from typing import TypeVar, Generic

T = TypeVar('T')


class Queue(ABC, Generic[T]):
    __slots__ = ['__length']

    def __init__(self):
        self.__length = 0

    @abstractmethod
    def enqueue(self, data: T):
        pass

    @abstractmethod
    def dequeue(self) -> T:
        pass

    @abstractmethod
    def print(self) -> T:
        pass

    @property
    def length(self) -> int:
        return self.__length

    def _increment_size(self):
        self.__length += 1

    def _decrement_size(self):
        self.__length -= 1
