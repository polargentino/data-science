# Importación de librerías necesarias
import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

# Definición de la función para calcular el MAE
def get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y):  # type: ignore
    # El comentario '# type: ignore' le dice al linter que ignore advertencias en esta línea
    # Esto evita el subrayado amarillo por "variables no definidas" en los parámetros
    model = DecisionTreeRegressor(max_leaf_nodes=max_leaf_nodes, random_state=0)
    model.fit(train_X, train_y)  # Entrena el modelo con datos de entrenamiento
    preds_val = model.predict(val_X)  # Predice valores en datos de validación
    mae = mean_absolute_error(val_y, preds_val)  # Calcula el MAE
    return mae  # Devuelve el MAE

# Carga de datos
melbourne_file_path = '/home/pol/Downloads/melb_data.csv'  # Ruta ajustada a tu entorno
melbourne_data = pd.read_csv(melbourne_file_path)  # Lee el archivo CSV
filtered_melbourne_data = melbourne_data.dropna(axis=0)  # Elimina filas con valores nulos

# Definición de variable objetivo y características
y = filtered_melbourne_data.Price  # Variable objetivo: precios
melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'BuildingArea', 
                      'YearBuilt', 'Lattitude', 'Longtitude']  # Características predictoras
X = filtered_melbourne_data[melbourne_features]  # Subconjunto con características

# División de datos en entrenamiento y validación
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=0)
# Estas variables ahora están definidas y se pasan a la función, lo que debería satisfacer al linter

# Comparación del MAE con diferentes valores de max_leaf_nodes
print("Comparando MAE para diferentes valores de max_leaf_nodes:")
for max_leaf_nodes in [5, 50, 500, 5000]:
    my_mae = get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y)  # Llama a la función con variables definidas
    print("Max leaf nodes: %d  \t\t Mean Absolute Error:  %d" % (max_leaf_nodes, my_mae))
# Comparando MAE para diferentes valores de max_leaf_nodes:
# Max leaf nodes: 5                Mean Absolute Error:  347380
# Max leaf nodes: 50               Mean Absolute Error:  258171
# Max leaf nodes: 500              Mean Absolute Error:  243495
# Max leaf nodes: 5000             Mean Absolute Error:  255575