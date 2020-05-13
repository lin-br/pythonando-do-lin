import unittest

from me.anagrammer import Anagrammer


class TestAnagrammer(unittest.TestCase):

    def test_should_indicate_true_if_finding_a_anagram_on_a_list(self):
        anagrammer = Anagrammer('documenting')
        self.assertTrue(anagrammer.is_has_anagram(['abc', 'ntmeingcudo']))

    def test_should_indicate_false_if_not_finding_a_anagram_on_a_list(self):
        anagrammer = Anagrammer('documenting')
        self.assertFalse(anagrammer.is_has_anagram(['to', 'do']))


if __name__ == '__main__':
    unittest.main()
