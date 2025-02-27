from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_argument("--headless")

driver = webdriver.Chrome(options=options)
driver.get("https://www.loteriasantafe.gov.ar/index.php/resultados/quini-6")

try:
    # Esperar hasta que el contenedor aparezca (máximo 10 segundos)
    contenedor = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.ui-outputpanel.ui-widget.form-group"))
    )

    # Extraer números ganadores
    numeros = contenedor.find_elements(By.CSS_SELECTOR, "div.cuadrado b")
    numeros_ganadores = [num.text for num in numeros]
    print("Números ganadores:", numeros_ganadores)

    # Extraer premios dentro del contenedor
    filas_premios = contenedor.find_elements(By.CSS_SELECTOR, "#form\\:j_idt45_data tr")
    premios = []
    for fila in filas_premios:
        columnas = fila.find_elements(By.TAG_NAME, "td")
        premio = {
            "Categoría": columnas[0].text,
            "Pozo $": columnas[1].text,
            "Ganadores": columnas[2].text,
            "Premio Individual $": columnas[3].text
        }
        premios.append(premio)

    print("\nPremios:")
    for premio in premios:
        print(premio)

except Exception as e:
    print("Error:", e)

finally:
    driver.quit()


