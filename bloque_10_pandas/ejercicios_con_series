import pandas as pd

# Crear las listas
marca = ['Camp', 'Camp', 'Petzl', 'Petzl', 'Edelrid', 'Edelrid', 'Edelrid', 'Black Diamond', 'Black Diamond', 'Mammut']
modelos = ['Energy', 'Jasper', 'Simba', 'Adjama New', 'Moe', 'Orion', 'Leaf','Xenes', 'Chaos', 'Ophir']
precios = [39.90, 56.00, 45.00, 75.00, 49.90, 99.90, 65.00, 119.90, 99.90, 55.00]

# Definir una Series con modelos como índices y precios como valores
productos = pd.Series(precios, index=modelos)

# Mostrar los modelos con precio menor que 70 euros
productos_baratos = productos[productos < 70]
print(productos_baratos)

# Definir una nueva Series con el precio original para todos los productos excepto para la marca "Edelrid"
precios_descuento = precios.copy()
for i in range(len(marca)):
    if marca[i] == 'Edelrid':
        precios_descuento[i] *= 0.9  # Aplicar un descuento del 10%

productos_descuento = pd.Series(precios_descuento, index=modelos)
print(productos_descuento)
