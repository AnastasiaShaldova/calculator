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
    count = 0.0
    while x >= y:
        x -= y
        count += 1
    else:
        x = multiply(x, 10)
        while x >= y:
            x -= y
            count += 0.1
    return count


def extract_percentage(number, percentage):
    """
    Функция извлекает процент из числа.

    :param number: Число.
    :param percentage: Процент, который нужно извлечь.
    :return: Результат извлечения процента от числа.
    """

    result = multiply(number, percentage)
    return divide(result, 100)


def exponentiation(number, degree):
    """
    Функция возводит число в степень.

    :param number: Число.
    :param degree: Степень.
    :return: Результат возведения числа в степень.
    """
    result = 1
    while degree > 0:
        result = multiply(result, number)
        degree -= 1
    return result


def sqrt(number):
    """
    Функция извлекает корень из числа.

    :param number: Число.
    :return: Результат извлечения корня из числа.
    """

    print(number ** 0.5)
    pass
    # result = divide(1, 2)
    # return exponentiation(number, result)


def factorial(number):
    """
    Функция вычисляет факториал числа.

    :param number: Число.
    :return: Результат вычисления факториала.
    """

    fact = 1
    while number > 1:
        fact = multiply(fact, number)
        number -= 1
    return fact


print(f'Результат сложения: {sum(3, 3)}')
print(f'Результат вычитания: {subtract(3, 2)}')
print(f'Результат умножения: {multiply(3, 625)}')
print(f'Результат деления: {divide(1, 2)}')
print(f'Результат извлечения процента от числа: {extract_percentage(100, 27)}')
print(f'Результат возведения числа в степень: {exponentiation(2, 1)}')
print(f'Результат извлечения корня из числа: {sqrt(25)}')
print(f'Результат вычисления факториала: {factorial(5)}')

correct_operations = ['+', '-', '*', '/', '%', '**', 'log']
