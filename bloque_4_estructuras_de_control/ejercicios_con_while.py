# Asigna un valor a la variable i.
i = 1

# Defina una estructura de control que solo imprima i una vez. Tienes que usar while sin estados de salida.
while i == 1:
    print(i)
    i += 1

# Asigna i el valor 0.
i = 0

# Crea una estructura de control que vaya incrementando i mientras i sea menor de 10.
while i < 10:
    # Comprueba si el valor de i es 6
    if i == 6:
        print("Ejecución terminada")
        break
    i += 1