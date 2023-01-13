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


def task_2_1():
    class Pet:
        def __init__(self, name, animal_type, age):
            self.__age = age
            self.__animal_type = animal_type
            self.__name = name

        def set_name(self, name):
            self.__name = name

        def set_animal_type(self, animal_type):
            self.__animal_type = animal_type

        def set_age(self, age):
            self.__age = age

        def get_name(self):
            return self.__name

        def get_animal_type(self):
            return self.__animal_type

        def get_age(self):
            return self.__age

        def __str__(self):
            return f'Имя: {pet.get_name()}\n' \
                   f'Тип: {pet.get_animal_type()}\n' \
                   f'Возраст: {pet.get_age()}'

    name = input('Введите имя вашего питомца: ')
    animal_type = input('Введите тип вашего животного: ')
    age = input('Введите возраст вашего питомца: ')

    pet = Pet(name, animal_type, age)

    print(pet)


def task_2_2():
    class Car:
        def __init__(self, year_model, make):
            self.__speed = 0
            self.__make = make
            self.__year_model = year_model

        def set_year_model(self, year_model):
            self.__year_model = year_model

        def set_make(self, make):
            self.__make = make

        def get_speed(self):
            return self.__speed

        def accelerate(self):
            self.__speed += 5

        def break_(self):
            self.__speed -= 5

    car = Car('1900', 'audi')

    for i in range(5):
        car.accelerate()
        print(f'Скорость составляет {car.get_speed()}')

    print()

    for i in range(5):
        car.break_()
        print(f'Скорость составляет {car.get_speed()}')


def task_2_3():
    class Information:
        def __init__(self, name, address, age, telephone_number):
            self.__telephone_number = telephone_number
            self.__age = age
            self.__address = address
            self.__name = name

        def set_name(self, name):
            self.__name = name

        def set_address(self, address):
            self.__address = address

        def set_age(self, age):
            self.__age = age

        def set_telephone_number(self, telephone_number):
            self.__telephone_number = telephone_number

        def get_name(self):
            return self.__name

        def get_address(self):
            return self.__address

        def get_age(self):
            return self.__age

        def get_telephone_number(self):
            return self.__telephone_number

        def __str__(self):
            return f'Имя: {self.get_name()}\n' \
                   f'Адрес: {self.get_address()}\n' \
                   f'Возраст: {self.get_age()}\n' \
                   f'Номер телефона: {self.get_telephone_number()}\n'

    my = Information('Max', 'Brovary', '18', '+38063548177')
    mum = Information('Oksana', 'Brovary', '16', '+3806777897')
    dad = Information('Vova', 'Brovary', '11', '+3806399009')

    print(f'{my}\n{mum}\n{dad}')


if __name__ == '__main__':
    task_2_3()
