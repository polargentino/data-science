import requests
from bs4 import BeautifulSoup

# URL de los resultados del Quini 6
url = "https://www.loteriasantafe.gov.ar/index.php/resultados/quini-6"

# Hacer la solicitud HTTP
response = requests.get(url)

# Parsear el contenido HTML con BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Buscar todos los títulos de sorteos
titulos = soup.find_all("h3")

# Mostrar los títulos encontrados
for titulo in titulos:
    print("Sorteo:", titulo.text.strip())

# Buscar los números sorteados (necesitas encontrar en qué etiquetas están)
numeros = soup.find_all("td")  # Prueba con "td", pero puede cambiar

# Mostrar los primeros números encontrados
for num in numeros[:10]:  
    print("Número:", num.text.strip())
# Sin respuesta...