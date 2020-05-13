import unittest


class TestFileAnagrammer(unittest.TestCase):

    def test_should_indicate_true_if_finding_a_anagram_in_a_file(self):
        file_anagrammer = FileAnagrammer('resources/wordlist.txt')
        self.assertTrue(file_anagrammer.check_with_word('documenting'))

    def test_should_indicate_false_if_not_finding_a_anagram_in_a_file(self):
        file_anagrammer = FileAnagrammer('resources/wordlist.txt')
        self.assertFalse(file_anagrammer.check_with_word('not_finding'))

    def test_should_get_a_result_with_all_anagram_words(self):
        file_anagrammer = FileAnagrammer('resources/wordlist.txt')
        result = file_anagrammer.get_result_of_anagram('documenting')
        self.assertNotEqual(0, result.numbers_anagram)

    def test_should_get_a_result_with_anagram_words_equal_zero_if_not_finding_a_anagram(self):
        file_anagrammer = FileAnagrammer('resources/wordlist.txt')
        result = file_anagrammer.get_result_of_anagram('not_finding')
        self.assertEqual(0, result.numbers_anagram)


if __name__ == '__main__':
    unittest.main()
