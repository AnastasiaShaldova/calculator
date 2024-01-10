class Equation:
    @staticmethod
    def equation(number=None, operation=None, result=None):
        if operation == '+':
            return result - number
        elif operation == '-':
            return result + number
        elif operation == '*':
            return result / number
        elif operation == '/':
            return result * number

