import requests
from faker import Faker

fake = Faker('es_ES')

# URL del formulario de Google
url = 'https://docs.google.com/forms/d/e/tuformulario/formResponse'

# Generar un número de teléfono falso con la nomenclatura de Venezuela
def generate_phone_number():
    area_code = '0' + fake.random_element(elements=('414', '424', '412', '416', '426'))  # Códigos de área de Venezuela
    number = ''.join([str(fake.random_digit()) for _ in range(7)])  # Número de teléfono (7 dígitos)
    return f'+58-{area_code}-{number}'  # Formato: +58-{código de área}-{número}

# Cambia 'entry.123456' por el nombre correcto del campo de teléfono que encontraste
data = {
    'entry.123456': fake.name(),  # Asegúrate de usar
}