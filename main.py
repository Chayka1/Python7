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


if __name__ == '__main__':
    task_1_1()
