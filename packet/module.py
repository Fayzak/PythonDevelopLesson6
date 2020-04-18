import math


# функция выводит самый большой делитель (не обязательно простой) числа.


def num_div_max(n):
    max_div = 1
    for i in range(n - 1, 1, -1):
        if n % i == 0:
            if max_div < i:
                max_div = i
    print(max_div)
    return max_div

# функция выводит каноническое разложение числа на простые множители;


def num_divs_canon(n):
    divs = [1]
    i = 2
    while i < n:
        if n % i == 0:
            divs.append(i)
            n //= i
        else:
            i += 1
    divs.append(int(n))
    canon_divs = []
    temp = 0
    for i in divs:
        if i == temp:
            continue
        canon_divs.append(i)
        canon_divs.append('^')
        canon_divs.append(divs.count(i))
        canon_divs.append('+')
        temp = i
    del canon_divs[-1]
    print(canon_divs)
    return canon_divs

# выводит самый большой простой делитель числа.


def num_div_max_simple(n):
    divs = [1]
    i = 2
    while i < n:
        if n % i == 0:
            divs.append(i)
            n //= i
        else:
            i += 1
    divs.append(int(n))
    max = 0
    for i in divs:
        temp = 0
        if temp < i:
            temp = i
            max = temp
    print(max)
    return max

# выводит список всех делителей числа;


def num_divs(n):
    divs = [1]
    i = 2
    while i < n:
        if n % i == 0:
            divs.append(i)
            n //= i
        else:
            i += 1
    divs.append(int(n))
    print(divs)
    return divs

# проверка числа на простоту (простые числа - это те числа у которых делители единица и они сами);


def num_simple(n):
    if n < 2:
        print('Число не составное и не простое')
        quit()
    elif n == 2:
        print('Простое число')
        quit()
    else:
        i = 2
        lim = int(math.sqrt(n))
        while i <= lim:
            if n % i == 0:
                print('Составное число')
                quit()
            i += 1
        print('Простое число')



