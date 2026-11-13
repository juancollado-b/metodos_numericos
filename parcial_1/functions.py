import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import splev, splrep

NEWTON_MAX_ITER = 200


def iteraciones_por_error(a, b, error_decimal):
    ineq = (np.log((b - a) * np.pow(10, error_decimal)) / np.log(2)) - 1
    return int(np.ceil(ineq))


def bisectriz_op(a, b, f, n):
    if n <= 0:
        print("El numero de iteraciones debe ser mayor a 0")
        return None

    f_a = f(a)
    f_b = f(b)
    if f_a * f_b > 0:
        print("El intervalo inicial no cumple con las condiciones del T. Bolzano")
        return None

    for _ in range(n):
        c = (a + b) / 2
        f_c = f(c)

        if f_c == 0:
            return c

        if f_a * f_c < 0:
            b = c
            f_b = f_c
        else:
            a = c
            f_a = f_c

    return (a + b) / 2


def newton_raphson(x, f, df, err_newton):
    x_a = x
    # Propongo un numero maximo de iteraciones, que de no cumplir determino no-convergenica
    for i in range(NEWTON_MAX_ITER):
        d_value = df(x_a)
        if d_value == 0:
            print(f"Derivada cero en iteracion {i + 1}. No aplica el metodo.")
            return None

        x_b = x_a - f(x_a) / d_value
        if abs(x_b - x_a) <= err_newton:
            return {"raiz": x_b, "iter": i + 1}
        x_a = x_b

    print(f"No converge para la cantidad de iteraciones definida ({NEWTON_MAX_ITER})")
    return None


def trapecios_c(a, b, n, f):
    h = (b - a) / (n-1)
    ptos = np.arange(a + h, b, h)
    y = f(ptos)
    sum_ev = np.sum(y)
    return (h / 2) * (f(a) + f(b) + 2 * sum_ev)


def cota_trapecios(a, b, n, f2):
    x = np.linspace(a, b, 10000)
    h = (b - a) / n
    M2 = np.max(np.abs(f2(x)))
    return (b - a) * (h**2) * M2 / 12


def simpson_c(a, b, n, f):
    if n % 2 != 0:
        return False

    h = (b - a) / (n-1)
    pares = f(np.arange(a + 2 * h, b, 2 * h))
    impares = f(np.arange(a + h, b, 2 * h))

    return (h / 3) * (f(a) + f(b) + 2 * np.sum(pares) + 4 * np.sum(impares))


def cota_simpson(a, b, n, f4):
    if n <= 0 or n % 2 != 0:
        raise ValueError("n debe ser positivo y par")

    x = np.linspace(a, b, 10000)
    M4 = np.max(np.abs(f4(x)))

    h = (b - a) / n

    return (b - a) * h**4 * M4 / 180


def interpolacion_s(puntos, paso=0.1):
    (x, y) = puntos
    spl = splrep(x, y)
    f = lambda x: splev(x, spl)
    f_2 = lambda x: splev(x, spl, der=2)
    return f, f_2


def euler(f, x0, y0, h, n):
    x = x0
    y = y0

    xs = [x]
    ys = [y]

    for _ in range(n):
        y = y + h * f(x, y)
        x = x + h

        xs.append(x)
        ys.append(y)

    return xs, ys

def heun(f, x0, y0, h, n):
    xs = [x0]
    ys = [y0]

    for _ in range(n):
        x = xs[-1]
        y = ys[-1]

        k1 = f(x, y)
        y_1 = y + h * k1
        k2 = f(x + h, y_1)

        k_promedio = (k1 + k2) / 2
        y_next = y + h * k_promedio

        xs.append(x + h)
        ys.append(y_next)

    return xs, ys