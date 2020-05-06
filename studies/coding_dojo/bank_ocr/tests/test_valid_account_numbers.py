import unittest

from studies.coding_dojo.bank_ocr.src.ocr.validator_account_numbers import ValidatorAccountNumbers


class TestValidAccountNumbers(unittest.TestCase):

    def test_should_get_true_with_account_numbers_valid(self):
        self.assertTrue(ValidatorAccountNumbers.is_valid('457508000'))

    def test_should_get_false_with_account_numbers_all_number_one(self):
        self.assertFalse(ValidatorAccountNumbers.is_valid('111111111'))

    def test_should_get_false_with_account_numbers_invalid(self):
        self.assertFalse(ValidatorAccountNumbers.is_valid('664371495'))


if __name__ == '__main__':
    unittest.main()
