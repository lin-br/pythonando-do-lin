class ReaderAccountNumber:
    __slots__ = ['_list', '_numbers']

    NUMBERS_MASKS = {
        ' _ | ||_|': '0',
        '     |  |': '1',
        ' _  _||_ ': '2',
        ' _  _| _|': '3',
        '   |_|  |': '4',
        ' _ |_  _|': '5',
        ' _ |_ |_|': '6',
        ' _   |  |': '7',
        ' _ |_||_|': '8',
        ' _ |_| _|': '9'
    }
    NUMBER_OF_CHARACTERS = 27
    NUMBER_OF_SPACES = 3
    NUMBER_OF_LINES_WITH_NUMBERS = 3

    def _split_text_and_get_list(self, text):
        return text.split('\n')[:self.NUMBER_OF_LINES_WITH_NUMBERS]

    def _join_characters_of_number(self, text_splited, initial, end):
        number = ''
        for part in text_splited:
            number += part[initial:end]
        return number

    def _get_list_number_from_three_cells_on_three_lines(self, text_splited):
        list_of_numbers = []
        for initial in range(0, self.NUMBER_OF_CHARACTERS, self.NUMBER_OF_SPACES):
            end = initial + self.NUMBER_OF_SPACES
            list_of_numbers.append(self._join_characters_of_number(text_splited, initial, end))
        return list_of_numbers

    def __init__(self, text):
        self._list = self._get_list_number_from_three_cells_on_three_lines(self._split_text_and_get_list(text))

    @property
    def numbers(self):
        result = ''
        for number in self._list:
            result += self.NUMBERS_MASKS.get(number)
        return result
