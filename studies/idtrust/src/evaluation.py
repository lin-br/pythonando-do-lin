class Evaluation:
    __slots__ = ['__grade', '__result']

    GRADE_MAX = 100

    def __init__(self):
        self.__grade = 0
        self.__result = False

    def __acept_grade(self, grade: int):
        if grade < 0 or grade > self.GRADE_MAX:
            raise ValueError('Grade not accept!')
        return grade

    def __grade_less_than_grade_min(self, grade: int) -> bool:
        return grade < 38

    def __round(self, grade: int):
        multiples_5 = [number for number in range(1, self.GRADE_MAX + 1) if number % 5 == 0]
        multiple_5_approximate = [number for number in multiples_5 if 0 < number - grade < 3]
        if len(multiple_5_approximate) == 1:
            return multiple_5_approximate.pop()
        return grade

    def add_grade(self, grade: int) -> None:
        accepted_grade = self.__acept_grade(grade)
        if self.__grade_less_than_grade_min(accepted_grade):
            self.__grade = accepted_grade
        else:
            self.__grade = self.__round(accepted_grade)
            self.__result = True

    @property
    def result(self):
        return self.__result

    @property
    def grade(self) -> int:
        return self.__grade
