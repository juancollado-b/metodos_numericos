import numpy as np
import functions

f = lambda x: -3/2 * np.exp(-np.sin(2*x)) - x
df = lambda x: 3*np.exp(-np.sin(2*x))*np.cos(2*x) - 1

res_1 = functions.aproximacion_raiz(f, df, 5, {"a": -2, "b": 10}, 0.0005)
print("Primer resultado:", res_1)

res_2 = functions.aproximacion_raiz(f, df, 5, {"a": -5, "b": -3.8}, 0.0005)
print("Segundo resultado:", res_2)

# error_bolzano = functions.aproximacion_raiz(f, df, 5, {"a": -5.5, "b": -5}, 0.0005)


functions.graficar_funcion(f, (res_1["raiz"], res_2["raiz"]),  (-5, 10))

