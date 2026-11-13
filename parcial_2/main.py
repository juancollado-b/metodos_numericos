import functions
import matplotlib.pyplot as plt
import numpy as np


def ej_1():
    f = lambda x: (
        2 * np.log((4 * x) - 7) + x**2 - x * (15 / 2) + (209 / 16) - 2 * np.log(4)
    )

    a = 2
    b = 4

    n_f = functions.iteraciones_por_error(a, b, 4)
    print("Iteraciones f:", n_f)
    raiz_f = functions.bisectriz_op(a, b, f, n_f)

    print("Raiz f:", raiz_f)

    # Aunque es posible aplicar el metodo de NR no es conveniente ya que cerca de la raiz las pendientes de las R tangente son pequeñas y eso va a aumentar el numero de iteraciones

    g = lambda x: (
        2 * np.log((4 * x) - 7) + x**2 - x * (13 / 2) + (209 / 16) - 2 * np.log(4)
    )

    n_g = functions.iteraciones_por_error(1.8, 2, 4)
    print("Iteraciones f:", n_g)
    raiz_g = functions.bisectriz_op(1.8, 2, g, n_g)

    print("Raiz g:", raiz_g)

    dg = lambda x: (8 / (4 * x - 7)) + 2 * x - (13 / 2)
    result = functions.newton_raphson(1.8, g, dg, 0.0001)
    if result is not None:
        print(
            f"Raiz encontrada: {result.get('raiz'):.4f} \nNumero de iteraciones: {result.get('iter')} \nError: {0.0001}"
        )


def ej_2():
    f = lambda x: 8 * np.exp(np.sin(x)) - x

    n_f = functions.iteraciones_por_error(3.5, 4, 6)

    a = 0
    b = functions.bisectriz_op(3.5, 4, f, n_f)
    print("RAIZ", b)
    intg_r = functions.riemman(a, b, 11, f)
    intg_t = functions.trapecios_c(a, b, 11, f)

    print("Integral Metodo Rimman", intg_r)
    print("Integral Metodo Trapecios compuestos", intg_t)

    f2 = lambda x: (8 * np.exp(np.sin(x))) * ((np.cos(x) ** 2) - np.sin(x))

    error_r = functions.cota_rimman(a, b, 11, f2)
    error_t = functions.cota_trapecios(a, b, 11, f2)

    print("Error Rimman", error_r)
    print("Error trapecios", error_t)


def ej_3():
    x = np.array([0, 1, 2, 4, 5, 8, 9])
    y = np.array([1.80, 2.07, 1.53, 1.98, 2.01, 1.65, 2.10])

    f, f2 = functions.interpolacion_s((x, y), 0.0001)

    intg_s = functions.simpson_c(0, 9, 10, f)
    intg_t = functions.trapecios_c(0, 9, 10, f)

    print(f"Integrap por Simpson: {intg_s}\nIntegral por trapecios: {intg_t}")
    error_trapecions = functions.cota_trapecios(0, 9, 10, f2)
    print(f"Error trapecios: {error_trapecions}")


def main():
    ej_3()


main()
