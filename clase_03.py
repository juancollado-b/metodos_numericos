import numpy as np
import no_lineales
def exp_f(x):
    return np.exp(-x) - x

try:
    op_1 = no_lineales.bisectriz_op(0, 50, exp_f,50)
    print(f"OP1: {op_1}")
except ValueError as error:
    print("Error:", error)

