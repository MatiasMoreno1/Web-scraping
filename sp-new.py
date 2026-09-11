from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd



driver = webdriver.Chrome()
driver.get("https://quotes.toscrape.com/")



contador_paginas = 0
continuar =True
datos = []






quotes = driver.find_elements(By.CLASS_NAME,"quote")
for quote in quotes:
    frases= quote.find_element(By.CLASS_NAME,"text")
    autores = quote.find_element(By.CLASS_NAME,"author")
    
    datos.append({
        "frase": frases.text,
        "autor": autores.text
    })
    



#driver.execute_script("window.scrollTo(0,1200);")
boton = driver.find_elements(By.CSS_SELECTOR, "li.next a")

while continuar:
    contador_paginas += 1
    print(f"Scraping en pagina N°{contador_paginas} y pagina actual{driver.current_url}")
    quotes = driver.find_elements(By.CLASS_NAME,"quote")
    for quote in quotes:
        frases = quote.find_element(By.CLASS_NAME,"text")
        autores = quote.find_element(By.CLASS_NAME,"author")

        datos.append({
            "frase":frases.text,
            "autor":autores.text
        })
    
    if boton:
        url_siguiente = boton[0].get_attribute("href")
        driver.get(url_siguiente)
        boton = driver.find_elements(By.CSS_SELECTOR, "li.next a")
        
        
    else:
        continuar = False

print(f"Total paginas {contador_paginas}" )       

print(f"cantidad de datos: {len(datos)}")

#print(f"URL ACTUAL: {driver.current_url}")

#df = pd.DataFrame(datos)
#print(df)    
#df.to_excel("datos_de_pensadores.xlsx", sheet_name="Pensadores", index=False)
driver.quit()