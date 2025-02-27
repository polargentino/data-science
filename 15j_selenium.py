from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_argument("--headless")

driver = webdriver.Chrome(options=options)
driver.get("https://www.loteriasantafe.gov.ar/index.php/resultados/quini-6")

time.sleep(5)  # Esperamos a que cargue la página

# Obtener todas las etiquetas div y span con texto
elements = driver.find_elements(By.XPATH, "//div | //span")

for element in elements:
    text = element.text.strip()
    if text:
        print(text)  # Muestra solo los elementos con texto

driver.quit()
