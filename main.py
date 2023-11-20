def sum(x, y):
    """
    Функция сложения.

    :param x: Первое число.
    :param y: Второе число.
    :return: Результат сложения.
    """
    return x + y


def subtract(x, y):
    """
    Функция вычитания.

    :param x: Первое число.
    :param y: Второе число.
    :return: Результат вычитания.
    """
    return x - y


def multiply(x, y):
    """
    Функция умножения.

    :param x: Первое число.
    :param y: Второе число.
    :return: Результат умножения.
    """
    result = 0
    i = 0
    while i < y:
        result += x
        i += 1
    return result


def divide(x, y):
    """
    Функция деления.

    :param x: Делимое число.
    :param y: Делитель.
    :return: Результат деления.
    """
    if y == 0:
        print('Деление на 0 запрещено!')
    pass


def extract_percentage(number, percentage):
    """
    Функция извлекает процент из числа.

    :param number: Число.
    :param percentage: Процент, который нужно извлечь.
    :return: Результат извлечения процента от числа.
    """
    pass


def exponentiation(number, degree):
    """
    Функция возводит число в степень.

    :param number: Число.
    :param degree: Степень.
    :return: Результат возведения числа в степень.
    """
    pass


def sqrt(number):
    """
    Функция возводит число в степень.

    :param number: Число.
    :return: Результат извлечения корня из числа.
    """
    sqrt = number ** (0.5)
    pass


def factorial(number):
    """
    Функция вычисляет факториал числа.

    :param number: Число.
    :return: Результат вычисления факториала.
    """
    # x = 1
    # result = 0
    # i = 0
    # while i < number:
    #     result += x
    #     i += 1

    fact = 1
    result = 0
    while number > 1:
        i = 0
        while i < number:
            result += fact
            i += 1
        number -= 1
    return result


print(f'Результат сложения: {sum(3, 3)}')
print(f'Результат вычитания: {subtract(3, 2)}')
print(f'Результат умножения: {multiply(3, 3)}')
print(f'Результат деления: {divide(3, 3)}')
print(f'Результат извлечения процента от числа: {extract_percentage(100, 25)}')
print(f'Результат возведения числа в степень: {exponentiation(4, 2)}')
print(f'Результат извлечения корня из числа: {sqrt(5)}')
print(f'Результат вычисления факториала: {factorial(5)}')

correct_operations = ['+', '-', '*', '/', '%', '**', 'log']
