a = ['Hello', 'World']
b = ['Python', 3.9]
c = 'HelloWordPython'

# Recorre todos los caracteres de c e imprimelos por pantalla.
for char in c:
    print(char)

# Muestra todos los valores de a.
for value in a:
    print(value)

# Muestra cada valor de a y b mostrando cada elemento de a con el de la misma posición de b sin utilizar los índices de posición.
for value_a, value_b in zip(a, b):
    print(value_a, value_b)

# Muestra en cada iteración el valor y su índice para los elementos de b.
for index, value in enumerate(b):
    print(f'Índice: {index}, Valor: {value}')