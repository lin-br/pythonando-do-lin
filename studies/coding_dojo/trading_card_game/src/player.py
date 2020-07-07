from deck import Deck


class Player:
    __slots__ = ['__health', '__mana', '__deck', '__hand']

    def __init__(self, deck: Deck):
        self.__mana = 0
        self.__health = 30
        self.__deck = deck
        self.__hand = list()

    @property
    def health(self):
        return self.__health

    @property
    def mana(self):
        return self.__mana

    @property
    def deck(self) -> Deck:
        return self.__deck

    @property
    def hand(self) -> list:
        return self.__hand

    def start_your_turn(self):
        number_cards_begin = 3
        while number_cards_begin is not 0:
            self.__hand.append(self.__deck.take())
            number_cards_begin -= 1
