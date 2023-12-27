def multiply(x, y):
    """
    The multiplication function.

    :param x: The first number.
    :param y: The second number.
    :return: The result of the multiplication.
    """

    decimal_x, decimal_y = str(float(x)).split('.'), str(float(y)).split('.')
    count_decimal = len(decimal_x[1]) + len(decimal_y[1])
    x, y = int(''.join(decimal_x)), int(''.join(decimal_y))
    result = 0
    i = 0
    while i < y:
        result += x
        i += 1
    str_res = list(str(result))
    str_res.insert(-count_decimal, '.')
    return float(''.join(str_res))


def divide(x, y):
    """
    The division function.

    :param x: A divisible number.
    :param y: Divider.
    :return: The result of the division.
    """

    if y == 0:
        return 'Деление на 0 запрещено!'

    def func(divisible, divisor):
        division_result = 0
        while divisible >= divisor:
            divisible -= divisor
            division_result += 1
        return division_result, divisible

    limit = 12
    int_result, float_result = func(x, y)
    final_result = str(int_result) + '.'
    while float_result != 0 and limit > 0:
        result = multiply(float_result, 10.0)
        int_result, float_result = func(result, y)
        final_result += str(int_result)
        limit -= 1
    return float(final_result)


def sqrt(number, sq=0.5, accuracy=0.0001):
    """
    The function extracts the root of a number.

    :param number: A number.
    :param sq: A sqrt.
    :param accuracy: Accuracy.
    :return: The result of extracting the root of a number.
    """

    guess = number
    while True:
        res = guess + divide(number, guess)
        next_guess = multiply(res, sq)
        if abs(next_guess - guess) < accuracy:
            return next_guess
        guess = next_guess


print(sqrt(4))
