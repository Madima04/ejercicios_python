import pandas as pd
import numpy as np

brand = ['Camp', 'Camp', 'Petzl', 'Petzl', 'Edelrid', 'Edelrid', 'Edelrid', 'Black Diamond', 'Black Diamond', 'Mammut']

models = ['Energy', 'Jasper', 'Simba', 'Adjama New', 'Moe', 'Orion', 'Leaf','Xenes', 'Chaos', 'Ophir']

prices = [39.90, 56.00, 45.00, 75.00, 49.90, 99.90, 65.00, 119.90, 99.90, 55.00]

df = pd.DataFrame({
    'Brand': brand,
    'Model': models,
    'Price': prices
})

# Mostrar la columna “Brand”
print(df['Brand'])

# Muestra la quinta fila
print(df.iloc[4])

# Modifica el precio del modelo “Energy” a 9999
df.loc[df['Model'] == 'Energy', 'Price'] = 9999

# Crea una nueva columna “Discount” con el valor 50 para cada fila
df['Discount'] = 50

# Crea un nuevo DataFrame que añada las columnas “Sales” y “Total”
df['Sales'] = np.random.randint(0, 500, df.shape[0])
df['Total'] = df['Price'] * df['Sales']

# Muestra la información para la marca “Edelrid”
print(df.loc[df['Brand'] == 'Edelrid'])

# Muestra todos los valores con un precio mayor que 70
print(df[df['Price'] > 70])

# Muestra la información del DataFrame ordenado por ventas
df = df.sort_values(by='Sales')
print(df)

# Usando la función apply cambia el formato a dos decimales
df = df.applymap(lambda x: '%.2f' % x if isinstance(x, float) else x)
print(df)

# Muestra la principal información de las variables estadísticas de las columnas de tipo numérico
print(df.describe(include=[np.number]))

# Muestra la principal información de las variables estadísticas de las columnas de tipo categórico
print(df.describe(include=[np.dtype('O')]))

# Muestra si hay algún valor nulo
print(df.isnull().any())

# Calcula el número de productos para cada marca
print(df['Brand'].value_counts())

# Guarda la información del DataFrame en un fichero xlsx
df.to_excel('output.xlsx')
