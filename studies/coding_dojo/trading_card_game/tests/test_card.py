from pytest import raises

from card import Card


def test_should_get_the_cost_of_mana_the_card():
    card = Card(4)
    assert card.cost == 4


def test_should_burst_error_if_the_cost_of_mana_is_less_than_1():
    with raises(ValueError):
        card = Card(-1)


def test_should_burst_error_if_the_cost_of_mana_is_greater_than_8():
    with raises(ValueError):
        card = Card(9)
