import numpy as np

# Definir un ndarray de una dimensión con los valores 100, 1, 1001 y 123.
array_1d = np.array([100, 1, 1001, 123])

# Mostrar los valores desde el primer elemento hasta el cuarto incluido.
print(array_1d[0:4])

# Mostrar el valor de la primera posición.
print(array_1d[0])

# Definir un ndarray con dos filas y cuatro columnas con los valores [1,1,1,1] y [2,2,2,2].
array_2d = np.array([[1,1,1,1], [2,2,2,2]])

# Mostrar los dos primeros valores.
print(array_2d[0, 0:2])

# Mostrar el valor de la primera fila y primera columna.
print(array_2d[0, 0])

# Mostrar los valores que sean mayores que 1.
print(array_2d[array_2d > 1])