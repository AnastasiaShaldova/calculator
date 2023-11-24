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

    return divide(multiply(number, percentage), 100)


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

    return number ** divide(1, 2)


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


def equation(number, result):
    """
        Функция вычисляет простые уравнения.

        :param number: Число.
        :param result: результат уравнения
        :return: Результат простого уравнения.
        """
    pass


def calculator():
    operation = input('Выберите оператор (+, -, /, *, **, x^1/2, %, n!, equation, history): ')
    number_1 = float(input('Введите первое число: '))
    number_2 = float(input('Введите второе число: '))

    if operation == '+':
        print(f'Результат сложения: {sum(number_1, number_2)}')
    elif operation == '-':
        print(f'Результат вычитания: {subtract(number_1, number_2)}')
    elif operation == '*':
        print(f'Результат умножения: {multiply(number_1, number_2)}')
    elif operation == '/':
        print(f'Результат деления: {divide(number_1, number_2)}')
    elif operation == '**':
        print(f'Результат возведения числа в степень: {exponentiation(number_1, number_2)}')
    elif operation == 'x^1/2':
        print(f'Результат извлечения корня из числа: {sqrt(number_1)}')
    elif operation == '%':
        print(f'Результат извлечения процента от числа: {extract_percentage(number_1, number_2)}')
    elif operation == 'n!':
        print(f'Результат вычисления факториала: {factorial(number_1)}')
    elif operation == 'history':
        print('Вывод истории операций.')
    else:
        print('Ошибка: неправильный оператор!')


if __name__ == "__main__":
    calculator()

