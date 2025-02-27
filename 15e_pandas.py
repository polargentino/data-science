# 🔗 5. Scraping de una página web para obtener datos en CSV
# Si una web muestra datos tabulares, puedes usar pandas y BeautifulSoup para extraerlos:
import pandas as pd

# URL con una tabla de datos
url = "https://example.com/datos"

# Leer las tablas en la página web
dfs = pd.read_html(url)

# Guardar la primera tabla en un CSV
dfs[0].to_csv("web_data.csv", index=False)

print("Datos web guardados en CSV.")
