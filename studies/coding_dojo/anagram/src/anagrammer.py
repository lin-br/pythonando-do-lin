from functools import reduce
from math import factorial


class Anagrammer:
    __slots__ = ['_word', '_word_sorted']

    def __init__(self, word: str):
        self._word = word
        self._word_sorted = self.__word_sorted(word)

    @staticmethod
    def __word_sorted(word: str):
        return sorted(''.join(word.split(' ')))

    def is_has_anagram(self, list_of_word: list):
        list_of_word_sorted = [sorted(word) for word in list_of_word]
        return self._word_sorted in list_of_word_sorted

    def get_the_result_of_anagrams(self, matrix_of_words: list):
        anagrams = [array for array in matrix_of_words if sorted(''.join(array)) == self._word_sorted]
        return Result(self._word, anagrams)

    def get_number_of_anagrams(self):
        letters_more_of_one_time = {
            letter: self._word.count(letter) for letter in self._word_sorted if self._word.count(letter) > 1
        }
        factorial_total = factorial(len(self._word_sorted))

        if len(letters_more_of_one_time) > 0:
            factorial_from_letters_repeated = reduce(lambda x, y: x * y,
                                                     map(lambda x: factorial(x), letters_more_of_one_time.values()))
            return factorial_total / factorial_from_letters_repeated
        else:
            return factorial_total


class Result:
    __slots__ = ['_word', '_anagrams', '_number_of_anagrams']

    def __init__(self, word: str, anagrams: list):
        self._word = word
        self._anagrams = anagrams
        self._number_of_anagrams = len(anagrams)

    @property
    def word(self):
        return self._word

    @property
    def anagrams(self):
        return self._anagrams

    @property
    def number_of_anagrams(self):
        return self._number_of_anagrams
