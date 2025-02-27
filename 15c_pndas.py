# 🔌 3. Extraer datos desde una base de datos y guardarlos en CSV
# Si tienes acceso a una base de datos SQL (MySQL, PostgreSQL, etc.), puedes extraer datos y guardarlos en un CSV.

# Ejemplo con SQLite:
import sqlite3
import pandas as pd

# Conectar a la base de datos
conn = sqlite3.connect("mi_base_de_datos.db")

# Ejecutar una consulta SQL
df = pd.read_sql_query("SELECT * FROM tabla_vehiculos", conn)

# Guardar los datos en un archivo CSV
df.to_csv("vehiculos.csv", index=False)

print("Datos exportados exitosamente.")
