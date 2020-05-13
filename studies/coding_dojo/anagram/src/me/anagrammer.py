class Anagrammer:
    __slots__ = ['_word', '_word_sorted']

    def __init__(self, word: str):
        self._word = word
        self._word_sorted = sorted(word)

    def is_has_anagram(self, list_of_word: list):
        list_of_word_sorted = [sorted(word) for word in list_of_word]
        return self._word_sorted in list_of_word_sorted
