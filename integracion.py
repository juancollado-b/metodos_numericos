import numpy as np

expon = lambda x: np.exp(x)
cuadr = lambda x: np.pow(x, 2)
print("cuad", cuadr(2))


def riemman(a, b, n, f):
    h = (b - a) / (n - 1)
    puntos_medios = np.arange(a + h / 2, b, h)
    y = f(puntos_medios)
    integ = sum(y) * h
    return integ


def cota_rimman(a, b, n, f2):
    x = np.linspace(a, b, 10000)
    h = (b - a) / (n - 1)
    M2 = np.max(np.abs(f2(x)))
    return M2 * (b - a) * (h**2) / 24


def trapecios_c(a, b, n, f):
    h = (b - a) / (n - 1)
    ptos = np.arange(a + h, b, h)
    y = f(ptos)
    sum_ev = np.sum(y)
    return (h / 2) * (f(a) + f(b) + 2 * sum_ev)


def cota_trapecios(a, b, n, f2):
    x = np.linspace(a, b, 10000)
    h = (b - a) / (n - 1)
    M2 = np.max(np.abs(f2(x)))

    print("M2 rimman", M2)
    return (b - a) * (h**2) * M2 / 12


def simpson_c(a, b, n, f):
    if n % 2 != 0:  # Cantidad de nodos par, cantidad de intervalos (n-1) impar
        return False

    h = (b - a) / (n - 1)
    pares = f(np.arange(a + 2 * h, b, 2 * h))
    impares = f(np.arange(a + h, b, 2 * h))

    return (h / 3) * (f(a) + f(b) + 2 * np.sum(pares) + 4 * np.sum(impares))


def cota_simpson(a, b, n, f4):
    if n % 2 != 0:
        raise ValueError("n debe ser par")

    x = np.linspace(a, b, 10000)
    M4 = np.max(np.abs(f4(x)))

    return (np.pow(b - a, 5) / np.pow(180 * n, 4)) * M4


def n_trapecios(a, b, error_deseado, f2, puntos=10000):
    if error_deseado <= 0 or b <= a:
        raise ValueError("Intervalo o error deseado inválido")

    x = np.linspace(a, b, puntos)
    M2 = np.max(np.abs(f2(x)))

    n = np.ceil(np.sqrt(((b - a) ** 3 * M2) / (12 * error_deseado)))

    return max(1, int(n))


def n_simpson(a, b, error_deseado, f4, puntos=10000):
    if error_deseado <= 0 or b <= a:
        raise ValueError("Intervalo o error deseado inválido")

    x = np.linspace(a, b, puntos)
    M4 = np.max(np.abs(f4(x)))

    n = np.ceil(((b - a) ** 5 * M4 / (180 * error_deseado)) ** (1 / 4))

    # Simpson 1/3 necesita un número par de subintervalos
    n = max(2, int(n))

    if n % 2 != 0:
        n += 1
    return n


result_r = riemman(0, 1, 34, expon)
result_t = trapecios_c(0, 2, 34, cuadr)
result_s = simpson_c(0, 2, 34, cuadr)
print("RESULT", result_r)
print("RESULT TRAPECIO", result_t)
print("RESULT SIMPSON", result_s)
