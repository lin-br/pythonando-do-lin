from book import Book
from fifo import Fifo
from operations import Operations


def main():
    number_of_operations = int(input('How many operations? '))
    book = Book(Operations(Fifo()), number_of_operations)
    while book.can_add_operation is not False:
        book.add_operation(input('Input the operation: '))

    for x in range(0, number_of_operations):
        result = book.execute()
        if result is not None:
            print(result)


if __name__ == '__main__':
    main()
