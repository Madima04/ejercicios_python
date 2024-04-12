# Define una función llamada showAnimal que reciba dos argumentos name y n_legs e imprima esta información por pantalla.​

def mostrarAnimal(nombre, n_patas):
    print(f"El animal {nombre} tiene {n_patas} patas.")

# Define una función que puede recibir cualquier número de argumentos e imprima cuántos argumentos ha recibido.​

def contarArgs(*args):
    print(f"La función ha recibido {len(args)} argumentos.")

# Define una función que recibiendo dos números, devuelva la suma y la resta de ellos en una sola llamada.​

def sumarYRestar(a, b):
    return a + b, a - b

# Define una función que recibiendo dos números devuelva la multiplicación.​

def multiplicar(a, b):
    return a * b

# Define una función que recibiendo dos números devuelva el módulo.​

def modulo(a, b):
    return a % b

# Define una función que recibiendo una función del ejercicio 4 o ejercicio 5 y dos valores numéricos devuelva su resultado.

def aplicarFuncion(func, a, b):
    return func(a, b)

# Define una función que reciba el nombre y email de una persona. Si no recibe email, se asignará “Sin determinar”. La función debe imprimir el nombre y email de la persona.​

def mostrarPersona(nombre, email="Sin determinar"):
    print(f"Nombre: {nombre}, Email: {email}")

# Define una función que recibiendo un entero positivo, irá sumando este número a su anterior hasta llegar a 0 y devolverá el resultado final.​

def sumarHastaCero(n):
    if n < 0:
        raise ValueError("El número debe ser positivo")
    return sum(range(n + 1))

def sumarHastaCeroConWhile(n):
    if n < 0:
        raise ValueError("El número debe ser positivo")
    resultado = 0
    while n > 0:
        resultado += n
        n -= 1
    return resultado