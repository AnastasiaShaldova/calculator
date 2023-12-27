def amount(x, y):
    """
    The addition function.

    :param x: First number.
    :param y: Second number.
    :return: Result of addition.
    """

    return x + y


def subtract(x, y):
    """
    The subtraction function.

    :param x: First number.
    :param y: Second number.
    :return: The result of subtraction.
    """

    return x - y


def multiply(x, y):
    """
    The multiplication function.

    :param x: The first number.
    :param y: The second number.
    :return: The result of the multiplication.
    """
    def func(a, b):
        result = 0
        item = 0
        while item < b:
            result += a
            item += 1
        return result

    decimal_x, decimal_y = str(float(x)).split('.'), str(float(y)).split('.')
    count_decimal = len(decimal_x[1]) + len(decimal_y[1])
    x, y = int(''.join(decimal_x)), int(''.join(decimal_y))

    str_res = list(str(func(x, y)))
    str_res.insert(-count_decimal, '.')
    result = ''.join(str_res)
    return result


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
        divisible, divisor = float(divisible), float(divisor)
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
        int_result, float_result = func(float(result), float(y))
        final_result += str(int_result)
        limit -= 1

    return float(final_result)


def extract_percentage(number, percentage):
    """
    The function extracts a percentage from a number.

    :param number: A number.
    :param percentage: The percentage to be extracted.
    :return: The result of extracting a percentage of the number.
    """

    return divide(multiply(number, percentage), 100)


def exponentiation(number, degree):
    """
    The function raises the number to a power.

    :param number: A number.
    :param degree: Degree.
    :return: The result of exponentiation a number.
    """

    def func(x, y):
        final_result = 1
        while y > 0:
            final_result = multiply(final_result, x)
            y -= 1
        return final_result

    result = 0

    if int(degree) == degree and degree < 0:
        result = divide(1, func(number, abs(degree)))
    elif int(degree) == degree and degree > 0:
        result = func(number, degree)
    elif int(degree) != degree and degree > 0:
        decimal_degree = str(float(degree)).split('.')
        divisible = int(decimal_degree[0] + decimal_degree[1])
        divisor = int('1' + ('0' * len(decimal_degree[1])))
        result = sqrt(func(number, divisible), divisor)
        return result
    else:
        pass
    return result


def sqrt(number, sq=0.5, accuracy=0.0001):
    """
    The function extracts the root of a number.

    :param number: A number.
    :param sq: A sqrt.
    :param accuracy: Accuracy.
    :return: The result of extracting the root of a number.

    Args:

    """

    guess = number
    while True:
        res = guess + divide(number, guess)
        next_guess = multiply(res, sq)
        if abs(float(next_guess) - guess) < accuracy:
            return float(next_guess)
        guess = next_guess


def factorial(number):
    """
    The function calculates the factorial of a number.

    :param number: A number.
    :return: The result of calculating the factorial.
    """

    fact = 1
    while number > 1:
        fact = multiply(fact, number)
        number -= 1
    return fact


def equation(number=None, operation=None, result=None):
    """
    The function calculates simple equations.

    :param operation:
    :param number: A number.
    :param result: The result of the equation
    :return: The result of a simple equation.
    """

    if operation == '+':
        return result - number
    elif operation == '-':
        return result + number
    elif operation == '*':
        return result / number
    elif operation == '/':
        return result * number
