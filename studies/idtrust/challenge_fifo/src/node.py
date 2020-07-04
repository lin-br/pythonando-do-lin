class Node:
    __slots__ = ['__value', '__after']

    def __init__(self, value):
        self.__value = value
        self.__after = None

    @property
    def after(self):
        return self.__after

    @after.setter
    def after(self, after):
        self.__after = after

    @property
    def value(self):
        return self.__value
