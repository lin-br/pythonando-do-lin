class ValidatorAccountNumbers:

    @staticmethod
    def is_valid(numbers_in_text: str):
        total: int = 0
        for position, number in enumerate(numbers_in_text):
            place_inverted = (len(numbers_in_text) - position)
            total += place_inverted * int(number)
        return total % 11 == 0
