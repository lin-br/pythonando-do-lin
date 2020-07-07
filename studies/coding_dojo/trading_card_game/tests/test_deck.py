from card import Card
from deck import Deck


def test_should_the_size_of_deck_equal_a_quantity_of_cards_is_added():
    a_number = 6
    cards = [Card(number) for number in range(0, a_number)]
    deck = Deck(cards)
    assert len(deck) == a_number


def test_should_take_a_car_of_the_list_of_cards_is_added():
    card = Card(4)
    deck = Deck([card])
    assert deck.take() == card


def test_should_return_a_car_to_deck():
    card4 = Card(4)
    card0 = Card(0)
    deck = Deck([card4, card0])
    card_taked = deck.take()
    assert len(deck) == 1
    deck.return_card(card_taked)
    assert len(deck) == 2


def test_should_get_a_list_of_the_number_cards_per_mana():
    list_of_mana = [2, 2, 2, 5, 5, 8, 3]
    list_without_duplicates = list(set(list_of_mana))
    cards = [Card(number) for number in list_of_mana]
    deck = Deck(cards)
    dictionaries = [dictionary for dictionary in deck.get_number_cards_per_mana() for number in list_without_duplicates
                    if
                    dictionary['cost'] == number]
    for dictionary in dictionaries:
        assert dictionary['quantity'] == list_of_mana.count(dictionary['cost'])


def tes_should_shuffle_the_list_of_cards_when_a_card_is_returned():
    pass


def tes_should_shuffle_the_list_of_cards_when_a_list_of_cards_is_added():
    pass
