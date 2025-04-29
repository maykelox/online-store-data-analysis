import pandas as pd

# --- LIMPIEZA DE DATOS ---

# Cargar el archivo Excel
df = pd.read_excel("Online Retail.xlsx", engine='openpyxl')

# Mostrar primeras filas
print(df.head())

# Mostrar estructura general
print(df.info())

# Revisar columnas disponibles
print(df.columns)

# Eliminar filas con datos importantes faltantes
df = df.dropna(subset=['CustomerID'])

# Eliminar registros con valores inválidos (cantidad o precio)
df = df[(df['Quantity'] > 0) & (df['UnitPrice'] > 0)]

# Convertir el CustomerID a tipo texto
# Aunque los IDs son números, no se van a usar para hacer sumas ni operaciones matemáticas. Por eso los tratamos como texto (categoría):
df['CustomerID'] = df['CustomerID'].astype(str)

# Crear una columna nueva: TotalPrice
df['TotalPrice'] = df['Quantity'] * df['UnitPrice']

print(df.head())
print(df.describe())
print(df.info())

# --- ANÁLISIS DE CLIENTES Y VENTAS ---

# ¿Cuántos clientes únicos tiene la tienda?
clientes_unicos = df['CustomerID'].nunique()
print(f"Número de clientes únicos: {clientes_unicos}")

# ¿Cuánto se ha vendido en total?
ventas_totales = df['TotalPrice'].sum()
print(f"Ventas totales: £{ventas_totales:,.2f}")

# ¿Cuáles son los países con más ventas?
ventas_por_pais = df.groupby('Country')['TotalPrice'].sum().sort_values(ascending=False)
print(ventas_por_pais.head(10))

# ¿Cuáles son los productos más vendidos?
productos_mas_vendidos = df.groupby('Description')['Quantity'].sum().sort_values(ascending=False)
print(productos_mas_vendidos.head(10))

#¿Cuál es el ticket promedio por factura?
ticket_promedio = df.groupby('InvoiceNo')['TotalPrice'].sum().mean()
print(f"Ticket promedio por compra: £{ticket_promedio:,.2f}")

# Exportar los datos limpios a un .csv
df.to_csv("datos_limpios.csv", index=False)
