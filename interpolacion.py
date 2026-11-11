import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import splev, splrep


def common_graph_styles(axe: plt.Axes, title: str):
    axe.grid(True)
    axe.set_xlabel("x")
    axe.set_ylabel("y")
    axe.axhline(0, color="black", linewidth=0.5)
    axe.axvline(0, color="black", linewidth=0.5)
    axe.set_title(title)
    axe.legend()


def interpolacion_p(puntos):
    (x, y) = puntos
    if len(x) != len(y):
        raise ValueError("La cantidad de valores en x debe ser igual que en y")
    coeff = np.polyfit(x, y, len(x) - 1)
    f_polinomio = lambda x: np.polyval(coeff, x)

    return f_polinomio


def interpolacion_s(puntos, paso=0.1):
    (x, y) = puntos
    spl = splrep(x, y)
    f_spline = lambda x: splev(x, spl)
    return f_spline


def analisis_interpolacion(puntos, interpolacion, f, paso=0.1):
    (x, y) = puntos
    f_interp = interpolacion(puntos)
    xs = np.arange(x[0], x[-1] + paso, paso)
    ys = f_interp(xs)
    error = np.abs(f(xs) - ys)
    y_error_max = np.max(error)
    x_error_max = xs[np.argmax(error)]
    return {
        "puntos": (xs, ys),
        "error": error,
        "y_error_max": y_error_max,
        "x_error_max": x_error_max,
    }


def main():
    x = np.array([0.2, 0.8, 1.0, 1.4, 2.2, 2.7, 3.7, 4.2, 5.7, 6.1])
    y = np.array([0.2, 0.72, 0.84, 0.99, 0.81, 0.43, -0.53, -0.87, -0.55, -0.18])
    f = lambda x: np.sin(x)

    # Interpolacion Analisis
    datos_p = analisis_interpolacion((x, y), interpolacion_p, f)
    puntos_p = datos_p.get("puntos", ())
    datos_s = analisis_interpolacion((x, y), interpolacion_s, f)
    puntos_s = datos_s.get("puntos", ())

    # Graficos

    fig, (sline_ax, polin_ax, error_ax) = plt.subplots(3, 1, sharex=True)

    sline_ax.scatter(x, y, color="red", label="Datos")
    sline_ax.plot(*puntos_s, label="Spline", color="blue")
    sline_ax.plot(puntos_s[0], f(puntos_s[0]), label="Funcion original", color="green")
    common_graph_styles(sline_ax, "Spline Cubico")

    polin_ax.scatter(x, y, color="red", label="Datos")
    polin_ax.plot(*puntos_p, label="Polinomio ajustado", linestyle="-", color="red")
    polin_ax.plot(puntos_p[0], f(puntos_p[0]), label="Funcion original", color="green")
    common_graph_styles(polin_ax, "Polinomio Ajustado")

    error_ax.plot(
        puntos_p[0], datos_p.get("error"), label="Error Polinomio", color="purple"
    )
    error_ax.plot(puntos_s[0], datos_s.get("error"), label="Error Spline", color="red")
    error_ax.scatter(
        datos_p.get("x_error_max"), datos_p.get("y_error_max"), color="magenta"
    )
    error_ax.scatter(
        datos_s.get("x_error_max"), datos_s.get("y_error_max"), color="orange"
    )
    common_graph_styles(error_ax, "Error")
    plt.show()


# graficar_sline()
main()
