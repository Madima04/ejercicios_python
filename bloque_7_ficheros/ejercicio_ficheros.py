# Definir las líneas a escribir
linea1 = "Es mi primera línea."
linea2 = "Es mi segunda línea."
linea3 = "Es mi tercera línea."
linea4 = "¡Es el final del fichero!"

# Crear un archivo vacío llamado primerfichero.txt sin usar with
primerfichero = open('primerfichero.txt', 'w')
primerfichero.close()

# Crear un archivo vacío llamado segundofichero.txt usando with
with open('segundofichero.txt', 'w') as segundofichero:
    pass

# Escribir linea1 en primerfichero.txt
with open('primerfichero.txt', 'w') as primerfichero:
    primerfichero.write(linea1)

# Escribir linea2, linea3 y linea4 en segundofichero.txt, cada una en una nueva línea
with open('segundofichero.txt', 'w') as segundofichero:
    segundofichero.write(f"{linea2}\n{linea3}\n{linea4}")

# Leer primerfichero.txt y agregar su contenido al final de segundofichero.txt
with open('primerfichero.txt', 'r') as primerfichero:
    contenido = primerfichero.read()

with open('segundofichero.txt', 'a') as segundofichero:
    segundofichero.write(contenido)