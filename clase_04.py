import numpy as np
import no_lineales
f = lambda x: np.pow(x, 3) - 8
df = lambda x: 3*np.pow(x, 2)
# def f(x): return np.pow(x, 3) - 8
# def df(x): return 3*np.pow(x, 2)

result = no_lineales.newton_raphson((-100), f, df)
print("NEWTON {:.4f}".format(result))