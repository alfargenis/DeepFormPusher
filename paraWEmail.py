from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
from faker import Faker

# Configuración inicial de Selenium
driver = webdriver.Chrome()
fake = Faker('es_ES')

# Ir a Google y autenticarse
driver.get("https://accounts.google.com/signin")
time.sleep(2)

# Introduce el correo electrónico y la contraseña (uso de variables por seguridad)
username_input = driver.find_element(By.ID, "identifierId")
username_input.send_keys("tucorreo@gmail.com")
username_input.send_keys(Keys.ENTER)
time.sleep(2)

# Configura una espera explícita para el campo de contraseña
wait = WebDriverWait(driver, 10)
try:
    # Esperar hasta que el elemento de la contraseña esté presente en la página
    password_input = wait.until(EC.presence_of_element_located((By.NAME, "Passwd")))
    password_input.send_keys("tucontraseña")
    password_input.send_keys(Keys.ENTER)
except TimeoutException:
    print("El elemento de la contraseña no fue encontrado en el tiempo esperado.")

time.sleep(2)

# Navegar al formulario de Google Forms después de la autenticación
driver.get("https://docs.google.com/forms/d/e/tuformulario/formResponse")
time.sleep(2)

# Repetir el ciclo de llenado y envío del formulario
for _ in range(10000):  # Cambia 10000 por el número de veces que necesites
    nombre_usuario = fake.name()

    try:
        # Rellenar el campo de nombre de usuario                            
        driver.execute_script(f'document.getElementsByName("entry.912922422")[0].value="{nombre_usuario}";')  # Reemplaza "entry.912922422" con el nombre real del campo
    except Exception as e:
        print(f"Error al rellenar el campo de nombre de usuario: {e}")

    try:
        # Generar un correo electrónico aleatorio
        correo = fake.email()
        # Introducir el correo electrónico generado en el campo correspondiente
        driver.execute_script(f'document.getElementsByName("emailAddress")[0].value="{correo}";')
        print("Correo electrónico introducido correctamente.")
    except Exception as e:
        print(f"Error al introducir el correo electrónico: {e}")

    # Enviar el formulario
    try:
        driver.execute_script('document.forms[0].submit();')
        print("Formulario enviado correctamente.")
    except Exception as e:
        print(f"Error al enviar el formulario: {e}")

    # Esperar y verificar alertas
    try:
        WebDriverWait(driver, 2).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        alert.accept()
        print("Alerta cerrada.")
    except TimeoutException:
        print("No se encontró alerta.")

    # Esperar antes de recargar para el siguiente ciclo
    time.sleep(2)              
    driver.get("https://docs.google.com/forms/d/e/tuformulario/formResponse")  # Asegúrate de recargar la URL correcta

# Cerrar Selenium después de interactuar con el formulario
driver.quit()
