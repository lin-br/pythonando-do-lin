class ReaderAccountNumber:
    __slots__ = ['_list', '_numbers']

    _numbers_masks = {
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
    _number_of_characters = 27
    _number_of_spaces = 3
    _number_of_lines_with_numbers = 3

    def _split_text_and_get_list(self, text):
        return text.split('\n')[:self._number_of_lines_with_numbers]

    def _join_characters_of_number(self, text_splited, initial, end):
        number = ''
        for part in text_splited:
            number += part[initial:end]
        return number

    def _get_list_number_from_three_cells_on_three_lines(self, text_splited):
        list_of_numbers = []
        for initial in range(0, self._number_of_characters, self._number_of_spaces):
            end = initial + self._number_of_spaces
            list_of_numbers.append(self._join_characters_of_number(text_splited, initial, end))
        return list_of_numbers

    def __init__(self, text):
        self._list = self._get_list_number_from_three_cells_on_three_lines(self._split_text_and_get_list(text))

    @property
    def numbers(self):
        result = ''
        for number in self._list:
            result += self._numbers_masks.get(number)
        return result
