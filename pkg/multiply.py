class Multiply:
    @staticmethod
    def _multiply_numbers(a, b):
        result = 0
        while b:
            if b & 1:
                result += a
            a <<= 1
            b >>= 1
        return result

    @staticmethod
    def count_characters(x, y):
        dot_index_x = x.find('.')
        dot_index_y = y.find('.')

        chars_after_dot_x = 0
        chars_after_dot_y = 0

        if dot_index_x != -1:
            chars_after_dot_x = len(x) - dot_index_x - 1

        if dot_index_y != -1:
            chars_after_dot_y = len(y) - dot_index_y - 1

        total_chars_after_dot = chars_after_dot_x + chars_after_dot_y
        return total_chars_after_dot

    @staticmethod
    def remove_dots(x, y):
        if '.' in x:
            x = x.replace('.', '')
        if '.' in y:
            y = y.replace('.', '')
        return x, y

    @staticmethod
    def insert_decimal_point(number, position):
        if position == 0:
            return number
        str_number = list(str(number))
        str_number.insert(-position, '.')
        result = ''.join(str_number)
        return result

    @staticmethod
    def multiply(x, y):
        x, y = str(x), str(y)
        count_decimal = Multiply.count_characters(x, y)
        rm_dots = Multiply.remove_dots(x, y)
        res = Multiply._multiply_numbers(int(rm_dots[0]), int(rm_dots[1]))
        result = Multiply.insert_decimal_point(res, count_decimal)
        return result
