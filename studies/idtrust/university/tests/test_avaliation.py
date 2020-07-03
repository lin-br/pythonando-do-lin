import pytest

from evaluation import Evaluation


def test_should_evaluation_not_greater_than_100():
    evaluation = Evaluation()
    with pytest.raises(ValueError):
        evaluation.add_grade(101)


def test_should_evaluation_not_less_than_0():
    evaluation = Evaluation()
    with pytest.raises(ValueError):
        evaluation.add_grade(-42)


def test_should_evaluation_less_than_40_must_fail():
    evaluation = Evaluation()
    evaluation.add_grade(30)
    assert evaluation.result is False


def test_should_84_evaluation_have_to_be_85():
    evaluation = Evaluation()
    evaluation.add_grade(84)
    assert evaluation.grade == 85


def test_should_81_evaluation_not_have_to_be_85():
    evaluation = Evaluation()
    evaluation.add_grade(81)
    assert evaluation.grade == 81


def test_should_38_evaluation_not_have_to_be_40_and_must_fail():
    evaluation = Evaluation()
    evaluation.add_grade(38)
    assert evaluation.grade == 38 and evaluation.result is False
