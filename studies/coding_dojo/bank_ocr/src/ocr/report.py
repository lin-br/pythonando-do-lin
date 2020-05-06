from studies.coding_dojo.bank_ocr.src.ocr.reader_account_numbers import ReaderAccountNumber
from studies.coding_dojo.bank_ocr.src.ocr.validator_account_numbers import ValidatorAccountNumbers


class Report:
    @staticmethod
    def get_report_in_line(text):
        reader = ReaderAccountNumber(text)
        if '?' in reader.numbers:
            return f"{reader.numbers} ILL"
        elif not ValidatorAccountNumbers.is_valid(reader.numbers):
            return f"{reader.numbers} ERR"
        else:
            return reader.numbers
