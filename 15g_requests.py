import requests

url = "https://www.loteriasantafe.gov.ar/index.php/resultados/quini-6"
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url, headers=headers)
print(response.status_code)  # Verifica el código de respuesta
print(response.text[:1000])  # Muestra una parte del contenido obtenido
# El código 200 indica que la página se ha descargado correctamente, pero en el contenido solo aparecen etiquetas <script> y no los números del sorteo. Esto sugiere que la página carga los datos con JavaScript, lo que significa que requests no es suficiente para extraer la información.