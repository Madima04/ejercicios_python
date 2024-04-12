# Definir una variable con un string con el valor “ Master Python”.
variable = "   Master Python"

# Mostrar la longitud de la variable anterior.
print(len(variable))

# Mostrar el primer carácter del string.
print(variable[0])

# Mostrar el penúltimo carácter del string.
print(variable[-2])

# Eliminar los espacios iniciales del string.
variable_sin_espacios = variable.lstrip()
print(variable_sin_espacios)

# Mostrar los caracteres en posiciones impares.
print(variable_sin_espacios[::2])

# Convertir todo el string en minúscula.
variable_minuscula = variable_sin_espacios.lower()
print(variable_minuscula)

# Separar el string por espacios en blanco.
variable_separada = variable_minuscula.split()
print(variable_separada)

# Reemplazar “python” por “JAVA”.
variable_reemplazada = variable_minuscula.replace("python", "JAVA")
print(variable_reemplazada)