from pytest import fixture

from card import Card
from deck import Deck
from player import Player


@fixture
def deck():
    return Deck([
        Card(0), Card(0), Card(1), Card(1),
        Card(2), Card(2), Card(2), Card(2),
        Card(3), Card(3), Card(3), Card(3),
        Card(4), Card(4), Card(5), Card(5),
        Card(6), Card(6), Card(7), Card(8)
    ])


def test_should_a_player_begin_with_thirty_health(deck):
    assert Player(deck).health == 30


def test_should_a_player_begin_with_zero_mana():
    assert Player(deck).mana == 0


def test_should_a_player_begin_with_a_deck_of_twenty_damage_cards(deck):
    player = Player(deck)
    assert len(player.deck) == 20


def test_should_a_player_begin_with_a_deck_of_damage_cards_with_following_mana_costs(deck):
    player = Player(deck)
    for cost, quantity in player.deck.get_number_cards_per_mana():
        if cost == 0:
            assert quantity == 2
        if cost == 1:
            assert quantity == 2
        if cost == 2:
            assert quantity == 3
        if cost == 3:
            assert quantity == 4
        if cost == 4:
            assert quantity == 2
        if cost == 5:
            assert quantity == 2
        if cost == 6:
            assert quantity == 2
        if cost == 7:
            assert quantity == 1
        if cost == 8:
            assert quantity == 1


def test_should_a_player_receives_a_three_cards_has_initial_hand(deck):
    player = Player(deck)
    player.start_your_turn()
    assert len(player.hand) == 3
