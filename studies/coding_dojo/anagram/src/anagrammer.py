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
        letters_more_of_one_time = {}
        for letter in self._word_sorted:
            if self._word.count(letter) > 1:
                letters_more_of_one_time[letter] = self._word.count(letter)

        da = 0

        if len(letters_more_of_one_time) > 0:
            for number in letters_more_of_one_time.values():
                if da == 0:
                    da += factorial(number)
                else:
                    da *= factorial(number)

        factoriando = factorial(len(self._word_sorted))
        if da == 0:
            return factoriando
        else:
            return factoriando / da


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
