class Vehiculo:
    propietario = "Bosonit"

    def __init__(self, nombre, velocidad_maxima, kilometraje):
        self.nombre = nombre
        self.velocidad_maxima = velocidad_maxima
        self.kilometraje = kilometraje

    def capacidad(self, cap):
        return f"La capacidad de {self.nombre} es de {cap}."

class Autobus(Vehiculo):
    def capacidad(self, cap=50):
        return super().capacidad(cap)