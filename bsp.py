from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

driver = webdriver.Chrome()
driver.get("https://books.toscrape.com/")

datos =[]

continuar = True


div = driver.find_elements(By.CLASS_NAME, "product_pod")

for divs in div:
    titulo = divs.find_element(By.TAG_NAME,"h3")
    precio = divs.find_element(By.CLASS_NAME,"price_color")
    rating = divs.find_element(By.CSS_SELECTOR, "p.star-rating")
    rating.get_attribute("class")
    valoracion = rating.get_attribute("class").split()[1]
    
    datos.append({
        "titulos": titulo.text,
        "precios": precio.text,
        "valoraciones": valoracion
    })

boton = WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "li.next a"))
)
boton.click()

while True:
    
    div = driver.find_elements(By.CLASS_NAME, "product_pod")
    for divs in div:
        titulo = divs.find_element(By.TAG_NAME,"h3")
        precio = divs.find_element(By.CLASS_NAME,"price_color")
        rating = divs.find_element(By.CSS_SELECTOR, "p.star-rating")
        rating.get_attribute("class")
        valoracion = rating.get_attribute("class").split()[1]
        
        datos.append({
            "titulos": titulo.text,
            "precios": precio.text,
            "valoraciones": valoracion
        })
    boton = driver.find_elements(By.CSS_SELECTOR, "li.next a")
    if not boton:
        break
    boton[0].click()


df = pd.DataFrame(datos)
print(df)
df.to_csv("venta_libros.csv", index=False)
