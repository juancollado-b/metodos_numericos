import numpy as np

expon = lambda x: np.exp(x)
cuadr = lambda x: np.pow(x, 2)
print("cuad", cuadr(2))


def riemman(a, b, N, f):
    h = (b - a) / N
    puntos_medios = np.arange(a + h / 2, b, h)
    y = f(puntos_medios)
    integ = sum(y) * h
    return integ


def trapecios_c(a, b, n, f):
    h = (b - a) / n
    ptos = np.arange(a + h, b, h)
    y = f(ptos)
    sum_ev = np.sum(y)
    return (h / 2) * (f(a) + f(b) + 2 * sum_ev)


def cota_trapecios(a, b, n, f2):
    x = np.linspace(a, b, 10000)
    M2 = np.max(np.abs(f2(x)))

    return (np.pow(b - a, 3) / np.pow(12 * n, 2)) * M2


def simpson_c(a, b, n, f):
    if n % 2 != 0:
        return False

    h = (b - a) / n
    pares = f(np.arange(a + 2 * h, b, 2 * h))
    impares = f(np.arange(a + h, b, 2 * h))

    return (h / 3) * (f(a) + f(b) + 2 * np.sum(pares) + 4 * np.sum(impares))


def cota_simpson(a, b, n, f4):
    if n % 2 != 0:
        raise ValueError("n debe ser par")

    x = np.linspace(a, b, 10000)
    M4 = np.max(np.abs(f4(x)))

    return (np.pow(b - a, 5) / np.pow(180 * n, 4)) * M4


result_r = riemman(0, 1, 34, expon)
result_t = trapecios_c(0, 2, 34, cuadr)
result_s = simpson_c(0, 2, 34, cuadr)
print("RESULT", result_r)
print("RESULT TRAPECIO", result_t)
print("RESULT SIMPSON", result_s)
