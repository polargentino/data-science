# data-science
# Data Science Project

Este repositorio contiene códigos y análisis relacionados con proyectos de ciencia de datos.

## Archivos principales
- `test.py`: Script de prueba básico.
- `test_tensorflow.py`: Ejemplo de uso de TensorFlow.
- 

## Requisitos
- Python 3.x
- Bibliotecas principales: `numpy`, `pandas`, `tensorflow`

## Cómo ejecutar el proyecto
1. Clona este repositorio:
   ```bash
   git clone https://github.com/polargentino/data-science.git

## Comandos para subirlo bien y eliminar lo que salió mal
rm -rf .git
git init
git add README.md test.py test_tensorflow.py
git commit -m "first commit: Agregando archivos fundamentales (.py y README.md)"
git remote add origin git@github.com:polargentino/data-science.git
git push -u origin main


# Verificar el estado
git status

# Agregar los archivos modificados/nuevos
git add README.md new_script.py

# Realizar un commit
git commit -m "Agregando new_script.py y actualizando README.md"

# Subir los cambios
git push
--------------------------------------------------------------------------

## https://chatgpt.com/

📌 Paso a paso para usar Kaggle desde la terminal
1️⃣ Obtener la API Key de Kaggle
🛠️ Objetivo: Conseguir la clave de acceso para usar Kaggle desde la terminal.
1-Ir a la página de Kaggle:
👉 https://www.kaggle.com/
(Si no tienes cuenta, créala y luego inicia sesión).

2-Ir a la configuración de tu cuenta:

En la esquina superior derecha, haz clic en tu foto de perfil.
Luego selecciona "Account" (Cuenta).

3-Generar la API Key:

Baja hasta la sección "API".
Haz clic en "Create New API Token" (Crear nueva clave de API).
Se descargará un archivo llamado kaggle.json.
📌 Este archivo contiene tus credenciales (usuario y clave de acceso). ¡No lo compartas con nadie!

2️⃣ Configurar la API Key en tu máquina
🛠️ Objetivo: Permitir que la terminal use Kaggle sin pedir la clave cada vez.
Mover el archivo kaggle.json a la ubicación correcta:
Abre la terminal y ejecuta los siguientes comandos:

mkdir -p ~/.kaggle
mv ~/Descargas/kaggle.json ~/.kaggle/
chmod 600 ~/.kaggle/kaggle.json

🔹 mkdir -p ~/.kaggle → Crea la carpeta .kaggle en tu usuario si no existe.
🔹 mv ~/Descargas/kaggle.json ~/.kaggle/ → Mueve el archivo a la carpeta correcta. (Si descargaste el archivo en otra ubicación, cambia la ruta).
🔹 chmod 600 ~/.kaggle/kaggle.json → Protege el archivo para que solo tú puedas leerlo.

5-Verificar que la configuración es correcta:

Ejecuta el siguiente comando:

kaggle datasets list

Si todo está bien, verás una lista de datasets disponibles en Kaggle. ✅

3️⃣ Descargar un dataset desde Kaggle
🛠️ Objetivo: Descargar datasets para usarlos en proyectos de Data Science.
6-Buscar un dataset en Kaggle:
Supongamos que queremos descargar el dataset Melbourne Housing Snapshot (que ya viste en tu lista de datasets).
Primero, encuentra su nombre de referencia usando:

kaggle datasets list | grep "melbourne"

🔹 Esto buscará cualquier dataset que contenga "melbourne" en el título.

7-Descargar el dataset:
Usamos el nombre de referencia del dataset para descargarlo:

kaggle datasets download -d dansbecker/melbourne-housing-snapshot

🔹 -d → Especifica el dataset a descargar.
🔹 dansbecker/melbourne-housing-snapshot → Es el identificador del dataset.

Esto generará un archivo ZIP en la carpeta actual.

8-Extraer los datos:

unzip melbourne-housing-snapshot.zip -d melbourne_data

🔹 -d melbourne_data → Extrae los archivos dentro de una nueva carpeta llamada melbourne_data.

4️⃣ Cargar el dataset en Python
🛠️ Objetivo: Leer el archivo en un script de Python y analizarlo.
9-Abrir un script en Python y leer los datos con Pandas:
Abre tu archivo 6_melbourne_data.py y edita el contenido para incluir lo siguiente:

import pandas as pd

# Cargar los datos
df = pd.read_csv("melbourne_data/melb_data.csv")

# Mostrar información del dataset
print(df.describe())  # Resumen estadístico
print(df.head())      # Primeras 5 filas

10-Ejecutar el script en la terminal:

/home/pol/Desktop/data-science/env/bin/python /home/pol/Desktop/data-science/6_melbourne_data.py

Esto mostrará un resumen estadístico del dataset en la terminal.

🚀 ¡Y eso es todo!
Ahora ya sabes cómo:
✅ Obtener la API Key de Kaggle.
✅ Configurar la API Key en tu máquina.
✅ Descargar datasets desde Kaggle.
✅ Leer los datos en Python con Pandas.

🔹 Consejo: Guarda este paso a paso en un documento para futuras consultas. ¡Sigue practicando y avanza en Data Science! 🚀📊

