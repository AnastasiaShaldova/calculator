from calculator import amount, subtract, multiply, divide, exponentiation, sqrt, extract_percentage, factorial


def calculator():
    operation = input('Выберите оператор (+, -, /, *, **, x^, %, n!, equation, history): ')
    number_1 = float(input('Введите первое число: '))
    number_2 = float(input('Введите второе число: '))

    if operation == '+':
        print(f'Результат сложения: {amount(number_1, number_2)}')
        print(f'Результат сложения: {amount(number_1, number_2)}')
    elif operation == '-':
        print(f'Результат вычитания: {subtract(number_1, number_2)}')
    elif operation == '*':
        print(f'Результат умножения: {multiply(number_1, number_2)}')
    elif operation == '/':
        print(f'Результат деления: {divide(number_1, number_2)}')
    elif operation == '**':
        print(f'Результат возведения числа в степень: {exponentiation(number_1, number_2)}')
    elif operation == 'x^':
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
