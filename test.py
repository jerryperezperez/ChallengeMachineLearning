import requests

# URl definida al iniciar el servicio en modo local
url = 'http://localhost:5000/procesar'

# Definición del objeto JSON que es enviado como petición al servicio
datos = {
    "oraciones": [
        "Apple está buscando comprar una startup del Reino Unido por mil millones de dólares.",
        "San Francisco considera prohibir los robots de entrega en la acera."
    ]
}

# Se envía por el método POST y se almacena la respuesta en la variable response
response = requests.post(url, json=datos)

# Se imprime el estado del código y la respuesta generada por el servicio en formato JSON
print(response.status_code)
print(response.json())
