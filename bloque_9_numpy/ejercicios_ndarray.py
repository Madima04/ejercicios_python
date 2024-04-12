import numpy as np

# Definir un ndarray de una dimensión con los valores 5,8 y 9
arr = np.array([5, 8, 9])
print("Array:", arr)

# Mostrar su tamaño
print("Tamaño:", arr.size)

# Mostrar el dtype
print("Tipo de datos:", arr.dtype)

# Definir un ndarray con tres dimensiones y de tipo float usando como valores 5,8 y 9
arr_3d = np.array([[[5, 8, 9]]], dtype=float)
print("Array 3D:", arr_3d)

# Definir tres ndarray el primer con ceros, el segundo con unos y el último con todo vacío. 
# Todos ellos de una dimensión con tres columnas
zeros = np.zeros(3)
ones = np.ones(3)
empty = np.empty(3)

print("Array de ceros:", zeros)
print("Array de unos:", ones)
print("Array vacío:", empty)