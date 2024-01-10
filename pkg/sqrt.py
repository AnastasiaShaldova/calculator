# def sqrt(number, sq=0.5):

#     a = 0
#     b = int(number.split('.')[0])
#     epsilon = 0.00001
#
#     while abs(b - a) > epsilon:
#         c = divide((a + b), 2)
#         if exponentiation(c, sq) == number:
#             return c
#         elif exponentiation(c, sq) > number:
#             b = c
#         else:
#             a = c
#
#     return divide((a + b), 2)
#
#     accuracy = 0.0001
#     guess = number
#     while True:
#         res = guess + (guess - number)
#         next_guess = multiply(int(res), sq)
#         if abs(float(next_guess) - guess) < accuracy:
#             print(next_guess)
#             return next_guess
#         guess = next_guess
#
#     def sq(v, power=2):
