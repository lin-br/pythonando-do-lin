class Card:
    __slots__ = ['__cost']

    def __init__(self, cost_mana: int):
        self.__cost = cost_mana

    @property
    def cost(self) -> int:
        return self.__cost
