import unittest

from me.anagrammer import Anagrammer


class TestAnagrammer(unittest.TestCase):

    def test_should_indicate_true_if_finding_a_anagram_on_a_list(self):
        anagrammer = Anagrammer('documenting')
        self.assertTrue(anagrammer.is_has_anagram(['abc', 'ntmeingcudo']))

    def test_should_indicate_false_if_not_finding_a_anagram_on_a_list(self):
        anagrammer = Anagrammer('documenting')
        self.assertFalse(anagrammer.is_has_anagram(['to', 'do']))

    def test_should_get_the_result_of_anagrams_with_three_anagrams_given_a_matrix_contains_three_anagrams(self):
        anagrammer = Anagrammer('maria')
        matrix = [['ma', 'ria'], ['mm', 'ira'], ['ma', 'ri', 'a'], ['a', 'arim'], ['nothing']]
        result = anagrammer.get_the_result_of_anagrams(matrix)
        self.assertEqual(3, result.number_of_anagrams)

    def test_should_get_the_result_of_anagrams_without_anagrams_given_a_matrix_not_contains_anagrams(self):
        anagrammer = Anagrammer('maria')
        matrix = [['0', '1'], ['6', '1'], ['9', '34', '8'], ['23', '76'], ['000']]
        result = anagrammer.get_the_result_of_anagrams(matrix)
        self.assertEqual(0, result.number_of_anagrams)

    def test_should_the_result_of_anagrams_contains_a_list_with_two_anagrams_equals_topa_and_apot(self):
        anagrammer = Anagrammer('topa')
        matrix = [['to', 'pa'], ['tooooop', 'a'], ['t', 'op', 'pa'], ['pot', 'aa'], ['apot']]
        result = anagrammer.get_the_result_of_anagrams(matrix)
        self.assertListEqual([['to', 'pa'], ['apot']], result.anagrams)

    def test_should_the_result_of_anagrams_contains_the_word_from_anagram(self):
        anagrammer = Anagrammer('topa')
        result = anagrammer.get_the_result_of_anagrams([])
        self.assertEqual('topa', result.word)


if __name__ == '__main__':
    unittest.main()
