import unittest

from ocr.validator_account_numbers import ValidatorAccountNumbers


class TestValidAccountNumbers(unittest.TestCase):

    def test_should_get_true_with_account_numbers_valid(self):
        self.assertTrue(ValidatorAccountNumbers.is_valid('457508000'))


if __name__ == '__main__':
    unittest.main()
