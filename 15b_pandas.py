# 📝 2. Crear un CSV desde cero en Python
# Si tienes datos y quieres estructurarlos en un CSV, puedes hacerlo con pandas:
import pandas as pd

# Crear un diccionario con los datos
data = {
    "Brand": ["Toyota", "Ford", "BMW"],
    "Model": ["Corolla", "Focus", "X5"],
    "Year": [2020, 2018, 2022],
    "Engine_Size": [1.8, 2.0, 3.0],
    "Price": [20000, 18000, 50000]
}

# Convertirlo en un DataFrame
df = pd.DataFrame(data)

# Guardarlo como CSV
df.to_csv("mi_dataset.csv", index=False)

print("CSV guardado exitosamente.")
# Brand,Model,Year,Engine_Size,Price
# Toyota,Corolla,2020,1.8,20000
# Ford,Focus,2018,2.0,18000
# BMW,X5,2022,3.0,50000


