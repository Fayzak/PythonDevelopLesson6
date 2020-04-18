from packet import module
import unittest
import random
# Тестовые функции #


# 1 Test


def test_num_div_max_simple():
    """
    Проверка на простоту
    :return:
    """
    assert module.num_div_max_simple(9) == 3
    return True


# 2 Test


def test_num_divs():
    """
    Проверка на истинность вывода ВСЕХ делителей числа
    :return:
    """
    print()
    check = [2, 2, 3, 3, 7, 13]  # намеренно неправильно
    assert module.num_divs(3276) == check
    return True


# 3 Test


def factorial(num):
    if num == 0:
        return 1
    else:
        return num*factorial(num-1)


class TestNumSimple(unittest.TestCase):
    def test_num_simple(self):
        """
        Проверка на истинность результатов функции factorial при помощи Unittest
        :return:
        """
        self.assertEqual(factorial(5), 120)

# 4 Test


def num_div_min(n):
    """
    Находит минимальный (не обязательно простой) делитель числа
    :param n:
    :return:
    """
    min_div = n
    for i in range(n - 1, 1, -1):
        if n % i == 0:
            if min_div > i:
                min_div = i
    print(min_div)
    return min_div


def test_num_div_max():
    """
    Полуавтоматический метод тестирования при помощи сторонней функции :-)
    :return:
    """
    if module.num_div_max(1000) == (1000//num_div_min(1000)):
        print('True')
        return True
    else:
        print('False')
        return False


test_num_div_max()

# 5 Test


n = int(input('Введите любимое натуральное число: '))
s = input('Напечатайте каноническое разложение введенного числа в формате: x^n+y^i+... : ')
test_list = []
num_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
for i in s:
    if i in num_list:
        test_list.append(int(i))
    else:
        test_list.append(i)


def test_num_divs_canon():
    """
    Сочетание pytest при вводе данных (pytest -s)
    :return:
    """
    assert module.num_divs_canon(n) == test_list

# Dirty function test


random_list = ['Kate', 'Jake', 'Mark', 'Jacov', 'Robert']
temp_names = []
for i in range(1, 21):
    temp_names.append(random.choice(random_list))


def f(names, n):
    for j in range(1, n):
        names.append(random.choice(temp_names))
    return names


def test_f1():
    """
    Проверка на содержание заданного имени
    :return:
    """
    name = 'James'
    if name in f(temp_names, 10):
        return True
    else:
        return False


test_f1()


def test_f2():
    """
    Проверка на количество имен в списке (pytest -s)
    :return:
    """
    result = f(temp_names, 10)
    count = result.count('Jacob')
    try:
        assert int(input('Угадай, сколько раз имя содержится в списке: ')) == count
    except AssertionError:
        print('Ты не угадал')
