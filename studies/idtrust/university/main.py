from evaluation import Evaluation

if __name__ == '__main__':
    students = int(input('Students\' number:'))
    for number in range(0, students):
        evaluation = Evaluation()
        value_inputed = input('Put the grade:')
        evaluation.add_grade(int(value_inputed))
        print(f'The grade: {evaluation.grade}')
        print(f'The result: {evaluation.result}')
