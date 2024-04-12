import numpy as np

# Defina un ndarray de una dimensión con los valores 100, 999, 998, 997 y 997.
arr = np.array([100, 999, 998, 997, 997])

# Encuentra dónde está 997.
indices = np.where(arr == 997)

# Modifica todos los valores menores de 999 a 9999.
arr[arr < 999] = 9999

# Obtiene los valores únicos del ndarray.
unicos = np.unique(arr)

# Devuelve True si todos los valores son mayores que 1000.
todos_mayores = np.all(arr > 1000)

# Devuelve True si algún valor es mayor que 1000.
alguno_mayor = np.any(arr > 1000)

# Ordena el array en orden ascendente.
arr = np.sort(arr)