import numpy as np

# Definir un ndarray de una dimensión con los valores 5,8 y 9
arr = np.array([5, 8, 9])
print("Arreglo:", arr)

# Mostrar su tamaño
print("Tamaño:", arr.size)

# Mostrar el dtype
print("Tipo de datos:", arr.dtype)

# Definir un ndarray con tres dimensiones y de tipo float usando como valores 5,8 y 9
arr_3d = np.array([[[5, 8, 9]]], dtype=float)
print("Arreglo 3D:", arr_3d)

# Definir tres ndarray el primer con ceros, el segundo con unos y el último con todo vacío. 
# Todos ellos de una dimensión con tres columnas
ceros = np.zeros(3)
unos = np.ones(3)
vacio = np.empty(3)

print("Arreglo de ceros:", ceros)
print("Arreglo de unos:", unos)
print("Arreglo vacío:", vacio)
