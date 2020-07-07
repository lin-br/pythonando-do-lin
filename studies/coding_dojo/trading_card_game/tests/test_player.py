from pytest import fixture

from card import Card
from deck import Deck
from player import Player


@fixture
def list_of_mana():
    return [
        0, 0, 1, 1,
        2, 2, 2, 2,
        3, 3, 3, 3,
        4, 4, 5, 5,
        6, 6, 7, 8
    ]


@fixture
def deck(list_of_mana):
    return Deck([Card(number) for number in list_of_mana])


def test_should_a_player_begin_with_thirty_health(deck):
    assert Player(deck).health == 30


def test_should_a_player_begin_with_zero_mana():
    assert Player(deck).mana == 0


def test_should_a_player_begin_with_a_deck_of_twenty_damage_cards(deck):
    player = Player(deck)
    assert len(player.deck) == 20


def test_should_a_player_begin_with_a_deck_of_damage_cards_with_following_mana_costs(deck, list_of_mana):
    list_without_duplicates = list(set(list_of_mana))
    player = Player(deck)
    dictionaries = [dictionary for dictionary in player.deck.get_number_cards_per_mana() for number in
                    list_without_duplicates if dictionary['cost'] == number]
    for dictionary in dictionaries:
        assert dictionary['quantity'] == list_of_mana.count(dictionary['cost'])


def test_should_a_player_receives_a_three_cards_has_initial_hand(deck):
    player = Player(deck)
    player.start_your_turn()
    assert len(player.hand) == 3
