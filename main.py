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


def task_2_4():
    class Employee:
        def __init__(self, name, id_number, department, position):
            self.__position = position
            self.__department = department
            self.__id_number = id_number
            self.__name = name

        def set_name(self, name):
            self.__name = name

        def set_id_number(self, id_number):
            self.__id_number = id_number

        def set_department(self, department):
            self.__department = department

        def set_position(self, position):
            self.__position = position

        def get_name(self):
            return self.__name

        def get_id_number(self):
            return self.__id_number

        def get_department(self):
            return self.__department

        def get_position(self):
            return self.__position

        def __str__(self):
            return f'Имя: {self.get_name()}\n' \
                   f'Идентификационный номер: {self.get_id_number()}\n' \
                   f'Отдел: {self.get_department()}\n' \
                   f'Должность: {self.get_position()}'

    person1 = Employee('Сьюзан Мейерс', '47899', 'Бухгалтерия', 'Вице-президент')
    person2 = Employee('Марк Джоунс', '39119', 'IT', 'Программист')
    person3 = Employee('Джой Роджерс', '81774', 'Производственный', 'Инженер')

    print(f'{person1}\n\n'
          f'{person2}\n\n'
          f'{person3}')


def task_2_5():
    class RetailItem:
        def __init__(self, product_description, number_of_units, price):
            self.__price = price
            self.__number_of_units = number_of_units
            self.__product_description = product_description

        def set_product_description(self, product_description):
            self.__product_description = product_description

        def set_number_of_units(self, number_of_units):
            self.__number_of_units = number_of_units

        def set_price(self, price):
            self.__price = price

        def get_product_description(self):
            return self.__product_description

        def get_number_of_units(self):
            return self.__number_of_units

        def get_price(self):
            return self.__price

        def __str__(self):
            return f'Описание: {self.__product_description}\n' \
                   f'Количство на складе: {self.__number_of_units}\n' \
                   f'Цена: {self.__price}'

    product_1 = RetailItem('Пиджак', '12', '59.95')

    print(product_1)


def task_2_7():
    import pickle

    class Employee:
        def __init__(self, id, name, otdel, dolj):
            self.__id = id
            self.__name = name
            self.__otdel = otdel
            self.__dolj = dolj

        def set_id(self, id):
            self.__id = id

        def set_name(self, name):
            self.__name = name

        def set_otdel(self, otdel):
            self.__otdel = otdel

        def set_dolj(self, dolj):
            self.__dolj = dolj

        def get_id(self):
            return self.__id

        def get_name(self):
            return self.__name

        def get_otdel(self):
            return self.__otdel

        def get_dolj(self):
            return self.__dolj

    FIND = 1
    ADD = 2
    CHANGE = 3
    DEL = 4
    EXIT = 5

    try:
        file = open('manage.dat', 'rb')
        base = pickle.load(file)
        file.close()
    except FileNotFoundError:
        base = {}

    def main():
        print(base)
        menu()

    def menu():
        print()
        print('Меню.')
        print('---------')
        print('1. Найти сотрудника.')
        print('2. Добавить сотрудника.')
        print('3. Изменить имя, отдел и должность сотрудника.')
        print('4. Удалить сотрудника.')
        print('5. Выйти из программы.')
        print()
        choice = int(input('Выберите пункт меню: '))
        while choice < 1 or choice > 5:
            choice = int(input('Некорректный выбор, попробуйте снова: '))

        if choice == FIND:
            find()
            menu()
        elif choice == ADD:
            add()
            menu()
        elif choice == CHANGE:
            change()
            menu()
        elif choice == DEL:
            deleted()
            menu()
        elif choice == EXIT:
            file_dump = open('manage.dat', 'wb')
            pickle.dump(base, file_dump)
            file_dump.close()
            print('Словарь сохранён в manage.dat')
            exit()

    def find():
        user = input('Введите ID сотрудника для поиска: ')
        if user in base:
            print(base[user])
            print('Есть такой.')
        else:
            print('Не найдено.')

    def add():
        name = input('Имя: ')
        id = input('ID: ')
        otdel = input('Отдел: ')
        dolj = input('Должность:')
        obj = Employee(name, id, otdel, dolj)
        base[id] = obj

    def change():
        ID = input('ID сотрудника: ')
        if ID in base:
            name = input('Имя: ')
            otdel = input('Отдел: ')
            dolj = input('Должность:')
            obj = Employee(ID, name, otdel, dolj)
            base[ID] = obj
            print('Info. updated.')
            print(obj.get_name())
            print(obj.get_otdel())
            print(obj.get_dolj())
        else:
            print('Такого сотрудника нет.')

    def deleted():
        user = input('ID сотрудника: ')
        if user in base:
            del base[user]
            print('Сотрудник удалён.')
        else:
            print('Сотрудник не найден.')

    main()


def task_2_8():
    class Retailltem:
        def __init__(self, name, number_of_units, price):
            self.__name = name
            self.__number_of_units = number_of_units
            self.__price = price

        def set_name(self, name):
            self.__name = name

        def set_number_of_units(self, number_of_units):
            self.__number_of_units = number_of_units

        def set_price(self, price):
            self.__price = price

        def get_name(self):
            return self.__name

        def get_number_of_units(self):
            return self.__number_of_units

        def get_price(self):
            return self.__price

        def __repr__(self):
            return repr(self.__name)

    class CashRegister:
        def __init__(self):
            self.items = []

        def purchase_item(self, item):
            self.items.append(item)

        def get_total(self):
            total_price = 0
            for item in self.items:
                total_price += item.price
            return print(total_price)

        def show_items(self):
            for item in self.items:
                print(item.get_name() + ": " + str(item.get_price()))

        def clear(self):
            self.items = []

    product_1 = Retailltem('Пиджак', 12, 59.95)
    product_2 = Retailltem('Дизайнерские джинсы', 40, 34.95)
    product_3 = Retailltem('Рубашка', 20, 24.95)

    purchase_item = 1
    total = 2
    show = 3
    clear = 4
    quit = 5

    def main():
        print('Эта программа позволяет купить товар, находящийся в наличии')
        print('----------------------------')
        print('В магазине имеется:')
        print(product_1)
        print(product_2)
        print(product_3)
        choice = 0
        selected_product = 0

        while choice != quit:

            choice = get_menu_choice()

            if choice == purchase_item:
                number_of_product = input(f'Выберите товар:\n'
                                          f'1. {product_1}\n'
                                          f'2. {product_2}\n'
                                          f'3. {product_3} ')
                if number_of_product == 1:
                    selected_product = product_1
                elif number_of_product == 2:
                    selected_product = product_2
                elif number_of_product == 3:
                    selected_product = product_3
                    register.purchase_item(selected_product)
            elif choice == total:
                register.get_total()
            elif choice == show:
                register.show_items()
            elif choice == clear:
                register.clear()
            elif choice == quit:
                exit()

    def get_menu_choice():
        print('----------------------------')
        print('1.Добавить товар в корзину')
        print('2.Показать сумму покупки')
        print('3.Показать товары в корзине')
        print('4.Очистить корзину')
        print('5.Выйти из программы')
        choice = int(input('Введите соответствующий пункт меню: '))

        return choice

    register = CashRegister()
    main()


if __name__ == '__main__':
    task_2_8()
