class Multiply:
    @staticmethod
    def _multiply_numbers(a, b):
        result = 0
        item = 0
        while item < b:
            result += a
            item += 1
        return result

    @staticmethod
    def insert_decimal_point(number, position):
        str_number = list(str(number))
        str_number.insert(-position, '.')
        result = ''.join(str_number)
        return result

    @staticmethod
    def multiply(x, y):
        decimal_x, decimal_y = str(float(x)).split('.'), str(float(y)).split('.')
        count_decimal = len(decimal_x[1]) + len(decimal_y[1])
        x, y = int(''.join(decimal_x)), int(''.join(decimal_y))
        multiplied_result = Multiply._multiply_numbers(x, y)
        result = Multiply.insert_decimal_point(multiplied_result, count_decimal)
        return result
