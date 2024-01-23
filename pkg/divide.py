from pkg.multiply import Multiply


class Divider:
    @staticmethod
    def _perform_division(divisible, divisor):
        division_result = 0
        while divisible >= divisor:
            division_result += 1
            divisible >>= 1
        return division_result, divisible

    @staticmethod
    def divide(x, y):
        if y == 0:
            return 'Деление на 0 запрещено!'

        int_result, float_result = str(Divider._perform_division(x, y))
        final_result = str(int_result) + '.'

        limit = 12
        while float_result != 0 and limit > 0:
            print(float_result)
            result = Multiply.multiply(float_result, 10)
            int_result, float_result = Divider._perform_division(float(result), float(y))
            final_result += str(int_result)
            limit -= 1

        return final_result
