# Definir un conjunto con los valores coche, motocicleta, bicicleta
conjunto1 = {"coche", "motocicleta", "bicicleta"}

# Añadir avión al conjunto
conjunto1.add("avión")

# Eliminar coche del conjunto
conjunto1.remove("coche")

# Crear otro conjunto con los valores avión, coche, tractor
conjunto2 = set(["avión", "coche", "tractor"])

# Crear otro conjunto con los valores que se repitan en los conjuntos anteriores
conjunto3 = conjunto1.intersection(conjunto2)

# Mostrar un conjunto con todos los valores que pertenecen al conjunto creado en el punto 1 y punto 4
conjunto4 = conjunto1.union(conjunto2)

print("Conjunto 1:", conjunto1)
print("Conjunto 2:", conjunto2)
print("Conjunto 3:", conjunto3)
print("Conjunto 4:", conjunto4)