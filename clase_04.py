import numpy as np
import no_lineales

NEWTON_ERROR = 0.000001

# f = lambda x: np.pow(x, 3) - 8
# df = lambda x: 3 * np.pow(x, 2)

# f = lambda x: np.pow(x - 2, 3)
# df = lambda x: 3 * np.pow(x - 2, 2)

# f = lambda x: np.pow(x, 3) - 2 * x + 2
# df = lambda x: 3 * np.pow(x, 2) - 2 # Oscila no converge

f = lambda x: np.pow(x, 2) + 1
df = lambda x: 2*x # No tiene raices reales


result = no_lineales.newton_raphson(1, f, df, NEWTON_ERROR)
if result is not None:
    print(
        f"Raiz encontrada: {result.get('raiz')} \nNumero de iteraciones: {result.get('iter')} \nError: {NEWTON_ERROR}"
    )
