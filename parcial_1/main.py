import functions
import matplotlib.pyplot as plt
import numpy as np


def ej_1():
    f = lambda x: (
        (np.exp(np.pow(x, 4) - 4 * np.pow(x, 3) + 2 * np.pow(x, 2) + 8 * x - 8) + x - 3)
        / (x - 2)
    )
    g = lambda x: np.pow(x, 4) - 4 * np.pow(x, 3) + 2 * np.pow(x, 2) + 8 * x - 8
    a = 0
    b = 9 / 5
    xs = np.linspace(a, b, 50)
    ys = g(xs)

    plt.plot(xs, ys)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("f(x) - 1")

    plt.grid(True)
    plt.legend()
    # plt.show()  # Viendo el grafico se puede llegar a la conclusion de que en ese interavlo solo existe una raiz

    # Se puede aplicar metodo de biseccion ya que en los extremos del intervalo se cumple la condicion de bolzano
    n = functions.iteraciones_por_error(a, b, 4)
    print("N", n)
    x_0 = functions.bisectriz_op(a, b, g, n)

    print(f"Raiz {x_0:.4f}\nIteraciones: {n}")

    # Se puede aplicar NR ya que la ecuacion es derivable (y de facil derivacion), conviene hacerlo ya que este metodo
    # Tiene una convergencia mas rapida si podes estimar un punto cercano a la raiz (lo cual pudimos hacer por el grafico)
    # La unica desventaja es que si no pudiesemos elegir un buen punto de inicio el metodo podria divergir o converger a x=2 que es un 0 de la ecuacion pero la funcion no esta definida
    dg = lambda x: 4 * np.pow(x, 3) - 12 * np.pow(x, 2) + 4 * x + 8
    result = functions.newton_raphson(1, g, dg, 0.0001)
    if result is not None:
        print(
            f"Raiz encontrada: {result.get('raiz'):.4f} \nNumero de iteraciones: {result.get('iter')} \nError: {0.0001}"
        )


def ej_2():
    f = lambda x: np.sin(np.log(3 * x))
    # Despues de graficar me puedo dar cuenta que la primer raiz despues de uno esta dentro del intervalo [7,9]
    # Uso biseccion para aproximar la raiz
    n = functions.iteraciones_por_error(7, 9, 4)
    print("N", n)

    a = 1
    b = functions.bisectriz_op(7, 9, f, n)

    print(f"Raiz {b:.4f}\nIteraciones: {n}")

    intg_s = functions.simpson_c(a, b, 6, f)
    intg_t = functions.trapecios_c(a, b, 6, f)

    print(f"Integrap por Simpson: {intg_s}\nIntegral por trapecios: {intg_t}")

    f_2 = lambda x: (
        (np.sin(np.log(3 * x)) + np.cos(np.log(3 * x))) * (-1) / np.pow(x, 2)
    )
    f_4 = lambda x: (10 * np.sin(np.log(3 * x))) * (-1) / np.pow(x, 4)

    error_trapecions = functions.cota_trapecios(a, b, 6, f_2)
    error_simpson = functions.cota_simpson(a, b, 6, f_4)

    print(f"Cota trapecios: {error_trapecions}\nCota Simpson: {error_simpson}")


def ej_3():
    x = np.array([0, 1, 2, 3, 5, 7])
    y = np.array([1, 3, 8, 7, 2, 7])

    f, f_2 = functions.interpolacion_s((x, y))
    intg_s = functions.simpson_c(0, 7, 8, f)
    intg_t = functions.trapecios_c(0, 7, 7, f)

    print(f"Integrap por Simpson: {intg_s}\nIntegral por trapecios: {intg_t}")
    error_trapecions = functions.cota_trapecios(0,7,7, f_2)
    print(f"Error trapecios: {error_trapecions}")


def ej_4():
    def f(t, y):
        return np.exp(np.sin(t+y)) - 1

    t_0 = np.pi
    y_0 = 0.1
    t_f = 2*np.pi

    euler_1 = functions.euler(f,t_0, y_0, (t_f-t_0)/1, 1)
    print(f"Euler Pasos: 1")
    print(f"y(2*pi) = {euler_1[1][-1]:.8f}")

    euler_4 = functions.euler(f,t_0, y_0, (t_f-t_0)/4, 4)
    print(f"Euler Pasos: 4")
    print(f"y(2*pi) = {euler_4[1][-1]:.8f}")

    heaun_1 = functions.heun(f, t_0, y_0, (t_f-t_0)/1, 1)
    heaun_4 = functions.heun(f,t_0, y_0, (t_f-t_0)/4, 4)
    print(f"Heun Pasos: 1")
    print(f"y(2*pi) = {heaun_1[1][-1]:.8f}")
    print(f"Heun Pasos: 4")
    print(f"y(2*pi) = {heaun_4[1][-1]:.8f}")

    # Generar puntos intermedios
    t_dense = np.linspace(t_0, y_0, 10000)
    # Interpolar la solucion de Euler
    y_interp, _ = functions.interpolacion_s(euler_4, 0.0001)
    y_dense = y_interp(t_dense)

    # Evaluar segunda derivada
    def f2(t,y):
        return np.exp(2*np.sin(t+y)*np.cos(t+y))

    values = f2(t_dense, y_dense)

    # Maximo absoluto aproximado
    M2 = np.max(np.abs(values))

    # Cota de error local
    error_local = ((t_f-t_0)/4**2 / 2) * M2

    print(f"M2 aproximado: {M2:.8f}")
    print(f"Cota de error local: {error_local:.8f}")

def main():
    ej_4()


main()
