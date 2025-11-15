from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

# Configura WebDriver (puedes usar Chrome, Edge o Firefox)
driver = webdriver.Chrome()

# Accede a la página de todos los productos
url = "https://www.herbalife.com/es-es/u/category/all-products"
driver.get(url)
time.sleep(5)

# Elimina la ventana de filtrar
mostrar_todo = driver.find_element(By.XPATH, "//button[contains(.,'Mostrar 100 Resultado(s)')]")
mostrar_todo.click()
time.sleep(2)

# Haz clic en 'Carga más' tantas veces como sea necesario (10 veces para 100 productos, si aparecen 10 por página)
for _ in range(10):
    try:
        # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # time.sleep(2)
        load_more = driver.find_element(By.XPATH, "//button[contains(.,'Carga más')]")
        load_more.click()
        time.sleep(2)
    except:
        break  # Cuando ya no aparece el botón

# Extrae nombres, enlaces y presentaciones
productos = []
items = driver.find_elements(By.XPATH, "//a[contains(@href,'/u/products/')]")
for item in items:
    nombre = item.text
    print(nombre)
    enlace = item.get_attribute('href')
    productos.append({'Nombre': nombre, 'Enlace': enlace})

# Guarda como CSV
df = pd.DataFrame(productos)
df.to_csv('productos_herbalife.csv', index=False)

driver.quit()
