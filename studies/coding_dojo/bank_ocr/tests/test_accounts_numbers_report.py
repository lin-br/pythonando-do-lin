import unittest

from studies.coding_dojo.bank_ocr.src.ocr.report import Report


class TestAccountsNumbersReport(unittest.TestCase):

    def test_should_get_line_without_message_attemption(self):
        text = ' _  _  _  _  _  _  _  _    \n'
        text += '| || || || || || || ||_   |\n'
        text += '|_||_||_||_||_||_||_| _|  |\n'
        text += '                           '
        self.assertEqual('000000051', Report.get_report_in_line(text))

    def test_should_get_line_with_flag_ERR(self):
        text = ' _  _     _  _        _  _ \n'
        text += '|_ |_ |_| _|  |  ||_||_||_ \n'
        text += '|_||_|  | _|  |  |  | _| _|\n'
        text += '                           '
        self.assertEqual('664371495 ERR', Report.get_report_in_line(text))

    def test_should_get_line_with_flag_ILL_and_in_an_unidentified_digit_a_question_mark(self):
        text = '    _  _  _  _  _  _     _ \n'
        text += '|_||_|| || ||_   |  |  | _ \n'
        text += '  | _||_||_||_|  |  |  | _|\n'
        text += '                           '
        self.assertEqual('49006771? ILL', Report.get_report_in_line(text))

    def test_should_get_line_with_flag_ILL_and_in_the_unidentified_digits_a_question_mark(self):
        text = '    _  _     _  _  _  _  _ \n'
        text += '  | _| _||_| _ |_   ||_||_|\n'
        text += '  ||_  _|  | _||_|  ||_| _ \n'
        text += '                           '
        self.assertEqual('1234?678? ILL', Report.get_report_in_line(text))


if __name__ == '__main__':
    unittest.main()
