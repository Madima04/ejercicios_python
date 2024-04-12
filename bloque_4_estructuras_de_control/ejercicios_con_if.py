a = 10
b = 100

# Estructura de control para a
if a == 10:
    print("Es igual a 10")
else:
    print("Es diferente de 10")

# Estructura de control para a y b
if a == 10 and b == 10:
    print("Todos son igual a 10")
elif a == 10:
    print("Sólo a es igual a 10")
elif b == 10:
    print("B es igual a 10")
else:
    print("Ninguno es igual a 10")

# Estructura de control para verificar si a y b son impares
if a % 2 != 0 and b % 2 != 0:
    print("A y B son impares")
else:
    print("A y B no son impares")