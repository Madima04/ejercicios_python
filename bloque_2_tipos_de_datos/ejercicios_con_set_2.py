# Definir el diccionario usando dict()
diccionario = dict(coche=50, tren=75, barco=100)

# Definir el diccionario usando { }
diccionario = {"coche": 50, "tren": 75, "barco": 100}

# Definir el diccionario usando zip()
claves = ["coche", "tren", "barco"]
valores = [50, 75, 100]
diccionario = dict(zip(claves, valores))

# Mostrar los valores del diccionario
print(diccionario.values())

# Mostrar las claves del diccionario
print(diccionario.keys())

# Mostrar el valor de coche
print(diccionario["coche"])

# Añadir al diccionario avión con valor 100
diccionario["avión"] = 100

# Mostrar los elementos del diccionario
for clave, valor in diccionario.items():
    print(f"Clave: {clave}, Valor: {valor}")