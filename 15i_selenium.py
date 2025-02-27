from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Para ejecutar sin abrir el navegador (opcional)

driver = webdriver.Chrome(options=options)
url = "https://www.loteriasantafe.gov.ar/index.php/resultados/quini-6"
driver.get(url)

time.sleep(5)  # Esperamos que se cargue la página

# Imprimir el código HTML después de la carga
print(driver.page_source)

driver.quit()
