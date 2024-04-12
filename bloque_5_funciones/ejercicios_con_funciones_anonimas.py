# Función lambda que calcula el cuadrado de un número
cuadrado = lambda x: x ** 2

# Función lambda que devuelve True si el cuadrado de un número es mayor que 999, si no devuelve False
es_mayor = lambda x: cuadrado(x) > 999

# Función lambda que recibe dos números y devuelve el resultado de su multiplicación
multiplicacion = lambda x, y: x * y

# Utilizando la función sorted() y lambda para ordenar una lista de palabras teniendo en cuenta la segunda letra de cada palabra
lista_palabras = ['hola', 'mundo', 'python', 'programacion']
lista_ordenada = sorted(lista_palabras, key=lambda palabra: palabra[1])