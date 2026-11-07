import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import splrep, splev


def _estilo_grafico(axe, title):
    axe.grid(True)
    axe.set_xlabel("x")
    axe.set_ylabel("y")
    axe.axhline(0, color="black", linewidth=0.5)
    axe.axvline(0, color="black", linewidth=0.5)
    axe.set_title(title)


def interpolacion_p_ciclo(ciclo_cardiaco, paso=0.1):
    (x, y) = ciclo_cardiaco
    if len(x) != len(y):
        raise ValueError("La cantidad de valores en x debe ser igual que en y")
    coeff = np.polyfit(x, y, len(x) - 1)
    xs = np.arange(x[0], x[-1] + paso, paso)
    f_polinomio = lambda x: np.polyval(coeff, x)

    return (xs, f_polinomio, coeff)


def interpolacion_s_ciclo(ciclo_cardiaco, paso=0.1):
    (x, y) = ciclo_cardiaco
    spl = splrep(x, y)
    xs = np.arange(x[0], x[-1] + paso, paso)
    f_spline = lambda x: splev(x, spl)
    return (xs, f_spline)


def comando_polinomio(coeff, xs):
    integral_indefinida = np.polyint(coeff)

    return np.polyval(integral_indefinida, xs[-1]) - np.polyval(
        integral_indefinida, xs[0]
    )


def integ_trapecios(a, b, n, f):
    h = (b - a) / n
    ptos = np.arange(a + h, b, h)
    y = f(ptos)
    sum_ev = np.sum(y)
    return (h / 2) * (f(a) + f(b) + 2 * sum_ev)


def integ_simpson(a, b, n, f):
    if n % 2 != 0:
        return False

    h = (b - a) / n
    pares = f(np.arange(a + 2 * h, b, 2 * h))
    impares = f(np.arange(a + h, b, 2 * h))

    return (h / 3) * (f(a) + f(b) + 2 * np.sum(pares) + 4 * np.sum(impares))


def analisis_ciclo(ciclo_cardiaco):
    (x_polinomio, f_polinomio, coeff) = interpolacion_p_ciclo(ciclo_cardiaco)
    (x_spline, f_spline) = interpolacion_s_ciclo(ciclo_cardiaco)

    intg_polinomio_data = (x_polinomio[0], x_polinomio[-1], 80, f_polinomio)
    cmd_polinomio = comando_polinomio(coeff, x_polinomio)
    trapecios_polinomio = integ_trapecios(*intg_polinomio_data)
    simpson_polinomio = integ_simpson(*intg_polinomio_data)

    print(f"comando interpolador: {cmd_polinomio}")
    print(f"trapecios polinomio: {trapecios_polinomio}")
    print(f"simpson polinomio: {simpson_polinomio}")

    intg_spline_data = (x_spline[0], x_spline[-1], 800, f_spline)
    trapecios_spline = integ_trapecios(*intg_spline_data)
    simpson_spline = integ_simpson(*intg_spline_data)

    print(f"trapecios spline: {trapecios_spline}")
    print(f"simpson spline: {simpson_spline}")

    fig, (original_ax, polin_ax, spline_ax) = plt.subplots(3, 1, sharex=True)
    original_ax.plot(*ciclo_cardiaco)
    original_ax.scatter(*ciclo_cardiaco, color="red", marker="*")
    _estilo_grafico(original_ax, "Ciclo cardiaco original")

    polin_ax.plot(x_polinomio, f_polinomio(x_polinomio))
    polin_ax.scatter(*ciclo_cardiaco, color="red", marker="*")
    _estilo_grafico(polin_ax, "Polinomio interpolador")

    spline_ax.plot(x_spline, f_spline(x_spline))
    spline_ax.scatter(*ciclo_cardiaco, color="red", marker="*")
    _estilo_grafico(spline_ax, "Interpolacion Spliner")

    plt.show()
