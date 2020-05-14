class Anagrammer:
    __slots__ = ['_word', '_word_sorted']

    def __init__(self, word: str):
        self._word = word
        self._word_sorted = sorted(word)

    def is_has_anagram(self, list_of_word: list):
        list_of_word_sorted = [sorted(word) for word in list_of_word]
        return self._word_sorted in list_of_word_sorted

    def get_the_result_of_anagrams(self, matrix_of_words: list):
        anagrams = [array for array in matrix_of_words if sorted(''.join(array)) == self._word_sorted]
        return Result(self._word, anagrams)


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
