import requests
from faker import Faker

fake = Faker('es_ES')

# URL del formulario de Google
url = '/formResponse'

# Generar un número de teléfono falso con la nomenclatura de Venezuela
# Genera un número de teléfono en formato venezolano
def generate_phone_number():
    area_code = '0' + fake.random_element(elements=('414', '424', '412', '416', '426'))  # Códigos de área de Venezuela
    number = ''.join([str(fake.random_digit()) for _ in range(7)])  # Número de teléfono (7 dígitos)
    return f'+58-{area_code}-{number}'  # Formato: +58-{código de área}-{número}

# Cambia 'entry.123456' por el nombre correcto del campo de teléfono que encontraste
data = {
    'entry.': fake.name(),  # Asegúrate de usar el ID correcto para el campo de nombre
    'entry.': generate_phone_number()  # Asegúrate de usar el ID correcto para el campo de teléfono
}

# Contador de envíos exitosos inicializado antes de iniciar el bucle
successful_submissions = 0

# Número de envíos que deseas hacer
num_submissions = 10000  # Ajusta este número según tus necesidades

for _ in range(num_submissions):
    # Genera un nuevo nombre y número de teléfono para cada envío
    data['entry.'] = fake.name()
    data['entry.'] = generate_phone_number()

    response = requests.post(url, data=data)
    if response.status_code == 200:
        successful_submissions += 1  # Incrementa el contador de envíos exitosos
        print(f"Formulario enviado correctamente. Total envíos exitosos: {successful_submissions}")
    else:
        print(f"Error al enviar el formulario: {response.status_code}")
