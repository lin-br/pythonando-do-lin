from node import Node


class Queue:
    def __init__(self):
        self.__begin = None
        self.__last = None
        self.__length = 0

    def to_queue(self, number: int):
        if self.__begin is None:
            self.__begin = Node(number)
        elif self.__last is None:
            self.__last = Node(number)
        else:
            new = Node(number)
            self.__last.after = new
        self.__length += 1

    def dequeue(self) -> int:
        return self.__begin.value

    @property
    def length(self) -> int:
        return self.__length
