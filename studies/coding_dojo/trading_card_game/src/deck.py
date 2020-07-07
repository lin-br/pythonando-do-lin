from random import shuffle
from typing import List

from card import Card


class Deck:
    __slots__ = ['__list_card']

    def __init__(self, cards: List[Card]):
        self.__list_card = list(cards)
        shuffle(self.__list_card)

    def take(self) -> Card:
        return self.__list_card.pop()

    def return_card(self, card: Card):
        self.__list_card.append(card)
        shuffle(self.__list_card)

    def get_number_cards_per_mana(self) -> List[dict]:
        costs = [card.cost for card in self.__list_card]
        return [{'cost': x, 'quantity': costs.count(x)} for x in range(9)]

    def __len__(self) -> int:
        return len(self.__list_card)

    def __getitem__(self, card: Card):
        return self.__list_card.remove(card)

    def __contains__(self, card: Card) -> bool:
        return card in self.__list_card
