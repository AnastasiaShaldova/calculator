from pkg.multiply import Multiply


class Factorial:
    @staticmethod
    def factorial(number):
        result = 1
        while number > 1:
            result = Multiply.multiply(result, number)
            number -= 1
        return result
