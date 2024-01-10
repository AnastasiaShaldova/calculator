# def exponentiation(number, degree):
#     """
#     The function raises the number to a power.
#
#     :param number: A number.
#     :param degree: Degree.
#     :return: The result of exponentiation a number.
#     """
#
#     def func(x, y):
#         final_result = 1
#         while y > 0:
#             final_result = multiply(final_result, x)
#             y -= 1
#         return final_result
#
#     result = 0
#
#     if int(degree) == degree and degree < 0:
#         result = divide(1, func(number, abs(degree)))
#     elif int(degree) == degree and degree > 0:
#         result = func(number, degree)
#     elif int(degree) != degree and degree > 0:
#         decimal_degree = str(float(degree)).split('.')
#         divisible = int(decimal_degree[0] + decimal_degree[1])
#         divisor = int('1' + ('0' * len(decimal_degree[1])))
#         res = str(float(func(int(number), divisible))).split('.')
#         result = sqrt(res[0], divisor)
#         return result
#     else:
#         pass
#     return result
