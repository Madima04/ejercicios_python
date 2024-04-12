# Definir la primera lista
lista1 = [10, 20, 'Hello', 20.5]

# Añadir "Word" al final de la lista
lista1.append('Word')

# Añadir "Python" al principio de la lista
lista1.insert(0, 'Python')

# Eliminar el segundo valor de la lista
del lista1[1]

# Crear la segunda lista
lista2 = list((20, 40, 'Bye'))

# Unir las dos listas
lista_final = lista1 + lista2

# Mostrar la lista final
print(lista_final)