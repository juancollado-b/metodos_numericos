import numpy as np

import datos_ecg
import functions

ciclos_cardiacos = [
    (np.arange(0, 89), datos_ecg.Y[7:96]),
    (np.arange(0, 83), datos_ecg.Y[95:178]),
    (np.arange(0,73), datos_ecg.Y[177:250])
]


functions.analisis_ciclo(ciclos_cardiacos[0])
# functions.analisis_ciclo(ciclos_cardiacos[1])
# functions.analisis_ciclo(ciclos_cardiacos[2])


# ---------------- IMPORTANTE ------------------------

"""
La interpolación polinómica no es muy precisa para estos datos porque cada ciclo tiene muchos puntos,
lo que genera un polinomio de grado muy alto.
Estos polinomios suelen ser inestables y producen oscilaciones artificiales, especialmente en los extremos.
Como se puede observar en el extremo derecho del grafico, las integrales sobre este polinomio por lo tanto tambien son imprecisas
"""