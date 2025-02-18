import pandas as pd

# Crear un DataFrame de ejemplo
data = {
    "country": ["Argentina", "Brazil", "Chile", "Canada"],
    "population": [45000000, 213000000, 19000000, 38000000],
    "continent": ["South America", "South America", "South America", "North America"]
}

df = pd.DataFrame(data)

# Filtrar países con más de 1 millón de habitantes en Sudamérica
filtered_df = df[(df['population'] > 10**6) & (df['continent'] == 'South America')]

# Mostrar el resultado
print("Países con más de 1M de habitantes en Sudamérica:")
print(filtered_df)
# Países con más de 1M de habitantes en Sudamérica:
#     country  population      continent
# 0  Argentina    45000000  South America
# 1     Brazil   213000000  South America
# 2      Chile    19000000  South America