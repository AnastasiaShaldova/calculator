from pkg.divide import Divider
from pkg.multiply import Multiply


class Sqrt:

    @staticmethod
    def sqrt(number, sq=2):
        x = number
        while True:
            a = sq - 1
            b = float(Multiply.multiply(a, x))
            x1 = float(Divider.divide(float(Divider.divide(b + number, x ** a)), sq))
            if abs(x1 - x) < 0.0001:
                return x
            x = x1

        # guess = number
        # while True:
        #     next_guess = sq * (guess + (number / guess))
        #     if abs(next_guess - guess) < 0.0001:
        #         return next_guess
        #     guess = next_guess


print(Sqrt.sqrt(4194304, 10))
