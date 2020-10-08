from math import factorial, e


def combination(fro: int, to: int) -> float:
    return factorial(to) / factorial(to - fro) / factorial(fro)

def theorem_bernuli(k: int, n: int, p: float, q: float) -> float:
    return combination(k, n) * (p ** k) * (q ** (n - k))


def formula_puason(k: int, n: int, p: float) -> float:
    this_lambda = n * p
    return (this_lambda ** k) / factorial(k) * (e ** (-this_lambda))

def local_theorem_of_mavr_laplas()

print(formula_puason(1, 1000, 0.002))