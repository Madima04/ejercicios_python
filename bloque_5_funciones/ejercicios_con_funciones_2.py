import re

# Define una función que devuelva una lista con el doble de todos los elementos de la lista inicial.

def duplicar_elementos(lst):
    return [i * 2 for i in lst]

# Define una función que devuelva que eleve al cuadrado los elementos que sean pares.

def cuadrado_elementos_pares(lst):
    return [i ** 2 for i in lst if i % 2 == 0]

# Define una función que dada dos listas sume los elementos de la misma posición.​

def sumar_elementos(lst1, lst2):
    return [i + j for i, j in zip(lst1, lst2)]

# Define una función que dado una lista de strings devuelva una lista con el número de ‘a’ que aparece en cada string.​

def contar_a_en_cadenas(lst):
    return [s.count('a') for s in lst]

# Define una función que dado una lista sólo devuelva los elementos que son negativos.

def obtener_elementos_negativos(lst):
    return [i for i in lst if i < 0]

# Define una función que dado un string devuelva la lista de vocales que aparecen.

def obtener_vocales(s):
    return [c for c in s if c in 'aeiouAEIOU']

# Define una función que dado una lista devuelva la multiplicación de todos los elementos.

def multiplicar_elementos(lst):
    resultado = 1
    for i in lst:
        resultado *= i
    return resultado

# Dado un string extraer los números que aparecen en el texto y devolver su suma.

def sumar_numeros_en_cadena(s):
    numeros = re.findall(r'\d+', s)
    return sum(int(i) for i in numeros)

print(sumar_elementos([1, 2, 3], [4, 5, 6])) # [5, 7, 9]