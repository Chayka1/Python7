import random


def test_1():
    class Coin:
        def __init__(self):
            self.__sideup = 'Орел'

        def toss(self):
            if random.randint(0, 1) == 0:
                self.__sideup = 'Орел'
            else:
                self.__sideup = 'Решка'

        def get_sideup(self):
            return self.__sideup

        def __str__(self):
            return 'Подбрасываем...'

    my_coin = Coin()
    my_coin.toss()
    print(my_coin)
    print(my_coin.get_sideup())


def task_1_1():
    class My:
        def __init__(self):
            self.__my_car = '10'

        def go(self):
            return self.__my_car


def task_1_2():
    class Book:
        def __init__(self, book_title, author_name, publisher_name):
            self.__publisher_name = publisher_name
            self.__author_name = author_name
            self.__book_title = book_title

        def set_book_title(self, book_title):
            self.__book_title = book_title

        def set_author_name(self, author_name):
            self.__author_name = author_name

        def set_publisher_name(self, publisher_name):
            self.__publisher_name = publisher_name

        def get_book_title(self):
            return self.__book_title

        def get_author_name(self):
            return self.__author_name

        def get_publisher_name(self):
            return self.__publisher_name

        def __str__(self):
            return f'Заголовок книги: {self.get_book_title()}\n' \
                   f'Имя автора: {self.get_author_name()}\n' \
                   f'Имя издателя: {self.get_publisher_name()}\n'

    a = 'Гарри Поттер'
    b = 'Чайка Максим'
    c = 'Тарас Шевченко'

    book = Book(a, b, c)
    print(book)


if __name__ == '__main__':
    task_1_2()
