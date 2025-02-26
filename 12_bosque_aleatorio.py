import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

# 1. Cargar los datos
melbourne_file_path = '/home/pol/Downloads/melb_data.csv'  # Ruta al archivo CSV
melbourne_data = pd.read_csv(melbourne_file_path)  # Leer el archivo CSV en un DataFrame de pandas

# 2. Limpiar los datos (eliminar filas con valores faltantes)
melbourne_data = melbourne_data.dropna(axis=0)  # Eliminar filas con cualquier valor faltante

# 3. Definir la variable objetivo (y) y las características (X)
y = melbourne_data.Price  # La variable objetivo es el precio de la vivienda
melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'BuildingArea', 'YearBuilt', 'Lattitude', 'Longtitude']  # Lista de características a usar
X = melbourne_data[melbourne_features]  # Crear un DataFrame con las características seleccionadas

# 4. Dividir los datos en conjuntos de entrenamiento y validación
# Usamos train_test_split para dividir los datos en conjuntos de entrenamiento y validación.
# random_state=0 asegura que la división sea la misma cada vez que se ejecuta el código.
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=0)

# 5. Crear y entrenar el modelo de Bosque Aleatorio (Random Forest)
forest_model = RandomForestRegressor(random_state=1)  # Inicializar el modelo con random_state para reproducibilidad
forest_model.fit(train_X, train_y)  # Entrenar el modelo usando los datos de entrenamiento

# 6. Hacer predicciones en el conjunto de validación
melb_preds = forest_model.predict(val_X)  # Realizar predicciones usando el modelo entrenado

# 7. Evaluar el rendimiento del modelo usando el Error Absoluto Medio (MAE)
mae = mean_absolute_error(val_y, melb_preds)  # Calcular el MAE comparando las predicciones con los valores reales
print(mae)  # Imprimir el MAE
# Salida: 
# 191669.7536453626

# Gemini:
# Explicación Detallada:

# Carga de Datos:

# Se utiliza pandas para leer un archivo CSV que contiene datos de viviendas en Melbourne.
# La ruta del archivo se especifica en melbourne_file_path.
# pd.read_csv() carga los datos en un DataFrame de pandas, que es una estructura de datos tabular.
# Limpieza de Datos:

# dropna(axis=0) elimina todas las filas que contienen al menos un valor faltante. Esto asegura que el modelo se entrene solo con datos completos.
# Definición de Variables Objetivo y Características:

# y se asigna a la columna 'Price', que es la variable que queremos predecir (el precio de la vivienda).
# melbourne_features es una lista de las columnas que se utilizarán como características para hacer las predicciones (número de habitaciones, baños, tamaño del terreno, etc.).
# X se crea seleccionando solo las columnas especificadas en melbourne_features del DataFrame original.
# División de Datos:

# train_test_split() divide los datos en conjuntos de entrenamiento y validación.
# train_X y train_y son los datos de entrenamiento para las características y la variable objetivo, respectivamente.
# val_X y val_y son los datos de validación, que se utilizan para evaluar el rendimiento del modelo.
# random_state=0 asegura que la división sea consistente cada vez que se ejecute el código, lo cual es útil para la reproducibilidad.
# Creación y Entrenamiento del Modelo de Bosque Aleatorio:

# RandomForestRegressor() crea un modelo de bosque aleatorio para problemas de regresión.
# random_state=1 se utiliza para asegurar la reproducibilidad del modelo.
# forest_model.fit(train_X, train_y) entrena el modelo utilizando los datos de entrenamiento.
# Realización de Predicciones:

# forest_model.predict(val_X) utiliza el modelo entrenado para hacer predicciones sobre el conjunto de validación.
# Evaluación del Rendimiento:

# mean_absolute_error(val_y, melb_preds) calcula el Error Absoluto Medio (MAE), que mide la diferencia promedio entre las predicciones y los valores reales.
# El MAE se imprime en la consola, lo que proporciona una medida de la precisión del modelo.

