class Card:
    __slots__ = ['__cost']

    def __init__(self, cost_of_mana: int):
        self.__cost = self.__valid_cost_of_mana(cost_of_mana)

    @property
    def cost(self) -> int:
        return self.__cost

    @staticmethod
    def __valid_cost_of_mana(cost_of_mana):
        if cost_of_mana < 0 or cost_of_mana > 8:
            raise ValueError("The cost of mana doesn't less than 1 or greater than 8.")
        return cost_of_mana
