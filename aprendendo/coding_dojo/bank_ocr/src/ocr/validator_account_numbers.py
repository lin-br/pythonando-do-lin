class ValidatorAccountNumbers:

    @classmethod
    def is_valid(cls, numbers_in_text: str):
        aux: int = 9
        summ: int = 0
        for number in numbers_in_text:
            summ += int(number) * aux
            aux -= 1
        return summ % 11 == 0
