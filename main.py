from history import History
from pkg.amount import Amount
from pkg.divide import Divider
from pkg.equation import Equation
from pkg.exponentiation import Exponentiation
from pkg.extract_percentage import ExtractPercentage
from pkg.factorial import Factorial
from pkg.multiply import Multiply
from pkg.sqrt import Sqrt
from pkg.subtract import Subtract


class CalculatorApp:

    def __init__(self):
        self.history = History()
        self.amount_obj = Amount()
        self.subtract_obj = Subtract()
        self.multiply_obj = Multiply()
        self.divider_obj = Divider()
        self.equation_obj = Equation()
        self.exponentiation_obj = Exponentiation()
        self.extract_percentage_obj = ExtractPercentage()
        self.factorial_obj = Factorial()
        self.multiply_obj = Multiply()
        self.sqrt_obj = Sqrt()
        self.subtract_obj = Subtract()

    def run(self):
        while True:
            operation = input('Выберите оператор (+, -, /, *, **, x^, %, n!, history) или введите "exit" для выхода: ')
            if operation == "exit":
                break

            number_1 = None
            number_2 = None
            number = None

            if operation in ('+', '-', '*', '/', '**'):
                number_1 = float(input('Введите первое число: '))
                number_2 = float(input('Введите второе число: '))
            else:
                number = float(input('Введите число: '))

            if operation == '+':
                print(f'Результат сложения: '
                      f'{self.amount_obj.amount(number_1, number_2)}')
            elif operation == '-':
                print(f'Результат вычитания: '
                      f'{self.subtract_obj.sub(number_1, number_2)}')
            elif operation == '*':
                print(f'Результат умножения: '
                      f'{self.multiply_obj.multiply(number_1, number_2)}')
            elif operation == '/':
                print(f'Результат деления: '
                      f'{self.divider_obj.divide(number_1, number_2)}')
            elif operation == '**':
                print(f'Результат возведения числа в степень: '
                      f'{self.exponentiation_obj.exponentiation(number_1, number_2)}')
            elif operation == 'x^':
                print(f'Результат извлечения корня из числа: '
                      f'{self.sqrt_obj.sqrt(number)}')
            elif operation == '%':
                print(f'Результат извлечения процента от числа: '
                      f'{self.extract_percentage_obj.extract_percentage(number_1, number_2)}')
            elif operation == 'n!':
                print(f'Результат вычисления факториала: '
                      f'{self.factorial_obj.factorial(number)}')
            elif operation == 'history':
                self.history.show_history()
            else:
                print('Ошибка: неправильный оператор!')


calculator_app = CalculatorApp()
calculator_app.run()
