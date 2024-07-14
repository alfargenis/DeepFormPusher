import requests
from faker import Faker
import random

fake = Faker('es_ES')
url = '/formResponse'

successful_submissions = 0
num_submissions = 1000

for _ in range(num_submissions):
    data = {
        '': fake.name(),
        '': random.randint(24000000, 31000000),
        '': random.choice(['1', '2', '3', '4', '5'])
    }

    response = requests.post(url, data=data)
    if response.status_code == 200:
        successful_submissions += 1
        print(f"Formulario enviado correctamente. Total envíos exitosos: {successful_submissions}")
    else:
        print(f"Error al enviar el formulario: {response.status_code}")
