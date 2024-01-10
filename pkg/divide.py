from pkg.multiply import Multiply


class Divider:
    @staticmethod
    def divide(x, y):
        if y == 0:
            return 'Деление на 0 запрещено!'

        int_result, float_result = Divider._perform_division(x, y)
        final_result = str(int_result) + '.'

        limit = 12
        while float_result != 0 and limit > 0:
            result = Multiply.multiply(float_result, 10.0)
            int_result, float_result = Divider._perform_division(float(result), float(y))
            final_result += str(int_result)
            limit -= 1

        return float(final_result)

    @staticmethod
    def _perform_division(divisible, divisor):
        divisible, divisor = float(divisible), float(divisor)
        division_result = 0
        while divisible >= divisor:
            divisible -= divisor
            division_result += 1
        return division_result, divisible
