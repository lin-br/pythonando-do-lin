from me.anagrammer import Anagrammer


class FileAnagrammer:
    __slots__ = ['_path', '_full_list']

    def __init__(self, path_file: str):
        self._path = path_file
        self._full_list = self.__get_full_list_words(path_file)

    @staticmethod
    def __get_full_list_words(path_file: str):
        with open(path_file, 'r') as file:
            list_of_list_of_word = [line.lower().strip() for line in file]
        return list_of_list_of_word

    @staticmethod
    def __contains_allowed_letters(word: str, target: str):
        for letter in word:
            if word.count(letter) > target.count(letter):
                return False
        return True

    def check_with_word(self, word_for_check: str):
        anagrammer = Anagrammer(word_for_check)
        allowed_words = [word for word in self._full_list if self.__contains_allowed_letters(word, word_for_check)]
        words_together = [first + second for first in allowed_words for second in allowed_words]
        return anagrammer.is_has_anagram(words_together)

    def get_result_of_anagram(self, word_for_check: str):
        anagrammer = Anagrammer(word_for_check)
        allowed_words = [word for word in self._full_list if self.__contains_allowed_letters(word, word_for_check)]
        matrix = [[first, second] for first in allowed_words for second in allowed_words]
        return anagrammer.get_the_result_of_anagrams(matrix)
