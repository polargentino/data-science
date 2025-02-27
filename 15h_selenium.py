# Solución con Selenium 🚀
# Dado que los números se generan dinámicamente, necesitamos Selenium para simular un navegador y capturar los datos una vez que la página los haya cargado.

# Pasos para instalar Selenium y un controlador de navegador
# Instala Selenium:


# pip install selenium
# Descarga el WebDriver correspondiente a tu navegador:

# Chrome: Chromedriver
# Firefox: Geckodriver
# Edge: EdgeDriver
# Guarda el WebDriver en la misma carpeta del script o en una ruta accesible.

# Código para extraer los números de Quini 6
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Configurar Selenium con Chrome
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Ejecutar en segundo plano (opcional)

driver = webdriver.Chrome(options=options)  # Usa el driver correcto

# Ir a la página
url = "https://www.loteriasantafe.gov.ar/index.php/resultados/quini-6"
driver.get(url)

# Esperar a que se cargue la página completamente
time.sleep(5)  

# Extraer los números del sorteo
numeros = driver.find_elements(By.CLASS_NAME, "numero")  # Ajusta la clase según la estructura de la página

# Imprimir los números
for i, num in enumerate(numeros, start=1):
    print(f"Número {i}: {num.text}")

# Cerrar el navegador
driver.quit()

