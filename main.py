from calculator import amount, subtract, multiply, divide, exponentiation, sqrt, extract_percentage, factorial


def calculator():
    operations = {
        '+': amount,
        '-': subtract,
        '*': multiply,
        '/': divide,
        '**': exponentiation,
        'x^1/2': sqrt,
        '%': extract_percentage,
        'n!': factorial
    }

    operation = input('Выберите оператор (+, -, /, *, **, x^1/2, %, n!, equation, history): ')

    if operation == 'history':
        print('Вывод истории операций.')
        return

    if operation not in operations:
        print('Ошибка: неправильный оператор!')
        return

    number_1 = float(input('Введите первое число: '))
    number_2 = None
    if operation not in {'x^1/2', 'n!'}:
        number_2 = float(input('Введите второе число: '))

    result = operations[operation](number_1, number_2) if number_2 else operations[operation](number_1)
    print(f'Результат {operation}: {result}')


if __name__ == "__main__":
    calculator()
