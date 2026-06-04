import numpy as np
from scipy.interpolate import splrep, splev


import matplotlib.pyplot as plt

x=np.array([0.2,0.8,1.0,1.4,2.2,2.7,3.7,4.2,5.7,6.1])
y=np.array([0.2,0.72,0.84,0.99,0.81,0.43,-0.53,-0.87,-0.55,-0.18])

coeff=np.polyfit(x,y,len(x)-1) #puntos, grado
xs = np.arange(0.2,6.2,0.1)#para interpolación poner justo del primero a justo el final
ys = np.polyval(coeff, xs)
f= lambda x: np.sin(x)  
t=np.arange(0.2,6.2,0.1)
error=np.abs(f(xs)- ys)
y_error_max=np.max(error)
x_error_max = xs[np.argmax(error)]

spl = splrep(x, y)
x_fin = np.arange(0.2, 6.2, 0.1)
y_fin = splev(x_fin, spl)

error_sline = np.abs(f(x_fin) - y_fin)
y_serror_max = np.max(error_sline)
x_serror_max =x_fin[np.argmax(error_sline)]
def common_graph_styles(axe: plt.Axes, title: str):
    axe.grid(True)
    axe.set_xlabel("x")
    axe.set_ylabel("y")
    axe.axhline(0, color='black', linewidth=0.5)
    axe.axvline(0, color='black', linewidth=0.5)
    axe.set_title(title)
    axe.legend()

def graficar_sline():
    fig, (sline_ax, polin_ax, error_ax) = plt.subplots(3,1, sharex=True)

    sline_ax.scatter(x, y, color="red", label='Datos')
    sline_ax.plot(x_fin, y_fin, label="Sline", color="blue")
    sline_ax.plot(t, f(t), label="Funcion original", color="green")
    common_graph_styles(sline_ax, "Sline")

    polin_ax.scatter(x, y, color="red", label='Datos')
    polin_ax.plot(xs, ys, label='Polinomio ajustado', linestyle='-', color="red")
    polin_ax.plot(t, f(t), label="Funcion original", color="green")
    common_graph_styles(polin_ax, "Polinomio Ajustado")

    error_ax.plot(t, error, label="Error", color="purple")
    error_ax.plot(x_fin, error_sline, label="Error Sline", color="red")
    error_ax.scatter(x_error_max,y_error_max,color="magenta")
    error_ax.scatter(x_serror_max, y_serror_max, color="orange")
    common_graph_styles(error_ax, "Error")

    plt.show()

graficar_sline()