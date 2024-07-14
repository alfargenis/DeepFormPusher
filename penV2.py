from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

import random
import time
from faker import Faker

driver = webdriver.Chrome()
fake = Faker('es_ES')

# Ir a Google y autenticarse
driver.get("https://accounts.google.com/signin")
time.sleep(2)

# Introduce el correo electrónico y la contraseña
username_input = driver.find_element(By.ID, "identifierId")
username_input.send_keys("tuemail@example.com")
username_input.send_keys(Keys.ENTER)
time.sleep(2)

wait = WebDriverWait(driver, 10)
try:
    password_input = wait.until(EC.presence_of_element_located((By.NAME, "Passwd")))
    password_input.send_keys("tucontraseña")
    password_input.send_keys(Keys.ENTER)
except TimeoutException:
    print("El elemento de la contraseña no fue encontrado en el tiempo esperado.")

time.sleep(2)

# Navegar al formulario de Google Forms después de la autenticación
driver.get("https://docs.google.com/forms/d/e/tuformulario/viewform")    
time.sleep(2)

# Repetir el ciclo de llenado y envío del formulario 10000 veces
for _ in range(10000):
    # Generar datos falsos y rellenar campos de texto
    try:
        driver.execute_script(f'document.getElementsByName("entry.806418526")[0].value="{fake.name()}";')     
        driver.execute_script(f'document.getElementsByName("entry.2061521207")[0].value="{str(fake.random_int(min=24000000, max=31000000))}";')
    except Exception as e:
        print(f"Error al establecer otros campos ocultos: {e}")

    try:
        # Marcar el checkbox de correo electrónico si no está marcado
        email_checkbox = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@jsname='MPu53c']")))
        if not email_checkbox.get_attribute('aria-checked') == 'true':
            email_checkbox.click()
        print("Checkbox del correo electrónico marcado correctamente.")
    except Exception as e:
        print(f"Error al intentar marcar el checkbox del correo electrónico: {e}")

    try:
        # Seleccionar una opción de la sección aleatoriamente
        radio_options = wait.until(EC.visibility_of_all_elements_located((By.XPATH, "//div[@role='radio']")))
        random.choice(radio_options).click()
    except Exception as e:
        print(f"No se pudo seleccionar sección: {e}")

    try:
        # Enviar el formulario
        driver.execute_script('document.forms[0].submit();')
        print("Formulario enviado correctamente.")
    except Exception as e:
        print(f"Error al enviar el formulario: {e}")

    try:
        # Verificar alertas y cerrarlas
        WebDriverWait(driver, 2).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        alert.accept()
        print("Alerta cerrada.")
    except TimeoutException:
        print("No se encontró alerta.")

    # Recargar el formulario para el siguiente llenado
    time.sleep(2)
    driver.get("https://docs.google.com/forms/d/e/tuformulario/viewform")

# Cerrar Selenium después de interactuar con el formulario
driver.quit()
