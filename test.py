import requests

url = 'http://localhost:5000/procesar'
datos = {
    "oraciones": [
        "Apple está buscando comprar una startup del Reino Unido por mil millones de dólares.",
        "San Francisco considera prohibir los robots de entrega en la acera."
    ]
}

response = requests.post(url, json=datos)

print(response.status_code)
print(response.json())
