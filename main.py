from math import factorial, e, sqrt, pi


def combination(fro: int, to: int) -> float:
    return factorial(to) / factorial(to - fro) / factorial(fro)


def theorem_bernuli(k: int, n: int, p: float, q: float) -> float:
    '''
    :param k: number of successful attempt
    :param n: number of attempts
    :param p: successful probability
    :param q: unsuccessful attempt
    :return: result of theorem bernuli
    '''
    return combination(k, n) * (p ** k) * (q ** (n - k))


# write puason from to infinity
def formula_puason(k: int, n: int, p: float) -> float:
    this_lambda = n * p
    return (this_lambda ** k) / factorial(k) * (e ** (-this_lambda))


def gauss_function(x: float) -> float:
    return (e ** ((-x ** 2) / 2)) / sqrt(2 * pi)


# todo q get from p
def local_theorem_of_mavr_laplas(k: int, n: int, p: float, q: float) -> float:
    one_divided_by_sqr_of_npq = 1 / sqrt(n * p * q)
    x = (k - n * p) * one_divided_by_sqr_of_npq
    print('x={}'.format(x))
    return one_divided_by_sqr_of_npq * gauss_function(x)

# not very good
def local_theorem_of_mavr_laplas_range(k1: int, k2: int, n: int, p: float, q: float) -> float:
    total = 0
    for k in range(k2 - k1):
        total += local_theorem_of_mavr_laplas(k1 + k, n, p, q)
    return total


# result = 1
# for x in range(0, 3):
#     result -= formula_puason(x, 1000, 0.003)
#     print(x)
# print(result)

print(local_theorem_of_mavr_laplas_range(70, 301, 300, 0.25, 0.75))
