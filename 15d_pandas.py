# 🔄 4. Convertir un archivo Excel a CSV
# Si tienes un archivo Excel (.xlsx) y quieres convertirlo a CSV:
import pandas as pd

# Cargar el archivo Excel
df = pd.read_excel("datos.xlsx")

# Guardarlo como CSV
df.to_csv("datos_convertidos.csv", index=False)

print("Conversión exitosa.")
