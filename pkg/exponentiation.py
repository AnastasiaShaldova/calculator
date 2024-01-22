from pkg.divide import Divider
from pkg.multiply import Multiply
from pkg.sqrt import Sqrt


class Exponentiation:
    @staticmethod
    def power(x, y):
        result = 1
        while y > 0:
            result = Multiply.multiply(result, x)
            y -= 1
        return result

    @staticmethod
    def exponentiation(number, degree):
        result = 0

        if int(degree) == degree and degree < 0:
            result = Divider.divide(1, Exponentiation.power(number, abs(degree)))
        elif int(degree) == degree and degree > 0:
            result = Exponentiation.power(number, degree)
        elif int(degree) != degree and degree > 0:
            decimal_degree = str(degree).split('.')
            divisible = int(decimal_degree[0] + decimal_degree[1])
            divisor = int('1' + ('0' * len(decimal_degree[1])))
            res = float(Exponentiation.power(int(number), divisible))
            result = Sqrt.sqrt(res, divisor)
        else:
            pass
        return result
