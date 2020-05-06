import unittest

from studies.coding_dojo.bank_ocr.src.ocr.reader_account_numbers import ReaderAccountNumber


class TestReadAccountNumbers(unittest.TestCase):

    def test_should_get_nine_numbers_zero(self):
        text = ' _  _  _  _  _  _  _  _  _ \n'
        text += '| || || || || || || || || |\n'
        text += '|_||_||_||_||_||_||_||_||_|\n'
        text += '                           '
        reader = ReaderAccountNumber(text)
        self.assertEqual('000000000', reader.numbers)

    def test_should_get_nine_numbers_one(self):
        text = '                           \n'
        text += '  |  |  |  |  |  |  |  |  |\n'
        text += '  |  |  |  |  |  |  |  |  |\n'
        text += '                           '
        reader = ReaderAccountNumber(text)
        self.assertEqual('111111111', reader.numbers)

    def test_should_get_nine_numbers_two(self):
        text = ' _  _  _  _  _  _  _  _  _ \n'
        text += ' _| _| _| _| _| _| _| _| _|\n'
        text += '|_ |_ |_ |_ |_ |_ |_ |_ |_ \n'
        text += '                           '
        reader = ReaderAccountNumber(text)
        self.assertEqual('222222222', reader.numbers)

    def test_should_get_nine_numbers_three(self):
        text = ' _  _  _  _  _  _  _  _  _ \n'
        text += ' _| _| _| _| _| _| _| _| _|\n'
        text += ' _| _| _| _| _| _| _| _| _|\n'
        text += '                           '
        reader = ReaderAccountNumber(text)
        self.assertEqual('333333333', reader.numbers)

    def test_should_get_nine_numbers_four(self):
        text = '                           \n'
        text += '|_||_||_||_||_||_||_||_||_|\n'
        text += '  |  |  |  |  |  |  |  |  |\n'
        text += '                           '
        reader = ReaderAccountNumber(text)
        self.assertEqual('444444444', reader.numbers)

    def test_should_get_nine_numbers_five(self):
        text = ' _  _  _  _  _  _  _  _  _ \n'
        text += '|_ |_ |_ |_ |_ |_ |_ |_ |_ \n'
        text += ' _| _| _| _| _| _| _| _| _|\n'
        text += '                           '
        reader = ReaderAccountNumber(text)
        self.assertEqual('555555555', reader.numbers)

    def test_should_get_nine_numbers_six(self):
        text = ' _  _  _  _  _  _  _  _  _ \n'
        text += '|_ |_ |_ |_ |_ |_ |_ |_ |_ \n'
        text += '|_||_||_||_||_||_||_||_||_|\n'
        text += '                           '
        reader = ReaderAccountNumber(text)
        self.assertEqual('666666666', reader.numbers)

    def test_should_get_nine_numbers_seven(self):
        text = ' _  _  _  _  _  _  _  _  _ \n'
        text += '  |  |  |  |  |  |  |  |  |\n'
        text += '  |  |  |  |  |  |  |  |  |\n'
        text += '                           '
        reader = ReaderAccountNumber(text)
        self.assertEqual('777777777', reader.numbers)

    def test_should_get_nine_numbers_eight(self):
        text = ' _  _  _  _  _  _  _  _  _ \n'
        text += '|_||_||_||_||_||_||_||_||_|\n'
        text += '|_||_||_||_||_||_||_||_||_|\n'
        text += '                           '
        reader = ReaderAccountNumber(text)
        self.assertEqual('888888888', reader.numbers)

    def test_should_get_nine_numbers_nine(self):
        text = ' _  _  _  _  _  _  _  _  _ \n'
        text += '|_||_||_||_||_||_||_||_||_|\n'
        text += ' _| _| _| _| _| _| _| _| _|\n'
        text += '                           '
        reader = ReaderAccountNumber(text)
        self.assertEqual('999999999', reader.numbers)

    def test_should_get_numbers_of_one_at_nine(self):
        text = '    _  _     _  _  _  _  _ \n'
        text += '  | _| _||_||_ |_   ||_||_|\n'
        text += '  ||_  _|  | _||_|  ||_| _|\n'
        text += '                           '
        reader = ReaderAccountNumber(text)
        self.assertEqual('123456789', reader.numbers)


if __name__ == '__main__':
    unittest.main()
