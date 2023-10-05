# Challenge de Reconocimiento de Entidades con Flask y SpaCy

Se ha empleado el microframework Flask y SpaCy para implementar un servicio web que procesa oraciones y retorna las entidades reconocidas por el modelo SpaCy.

## Requisitos principales

- Python
- Flask
- SpaCy
- Requests

## Configuración

De las dependencias correspondientes a SpaCy, se usaron los siguientes comandos:

```bash
pip install flask spacy requests
python -m spacy download es_core_news_sm
```
## Ejecución del servicio

Para iniciar el servicio, se debe ejecutar el siguiente comando:

```bash
python app.py
```

Esto permitirá inciar el servicio en http://localhost:5000/procesar.

## Prueba del servicio

Para la prueba y evaluación del servicio se puede emplear herramientas como Postman, pero para poder ejecutar pruebas
de forma directa, se ha creado un archivo de prueba, el cual se puede ejecutar con el siguiente comando:
```bash
python test.py
```

## Uso y demostración

El siguiente objeto JSON es el empleado como prueba en el archivo test.py.
```json
{
  "oraciones": [
    "Apple está buscando comprar una startup del Reino Unido por mil millones de dólares.",
    "San Francisco considera prohibir los robots de entrega en la acera."
  ]
}
```

El resultado generado de la ejecución del archivo de prueba es el siguiente objeto JSON:

```json
{
  "resultado": [
    {
      "entidades": {
        "Apple": "ORG",
        "Reino Unido": "LOC"
      },
      "oracion": "Apple está buscando comprar una startup del Reino Unido por mil millones de dólares."
    },
    {
      "entidades": {
        "San Francisco": "LOC"
      },
      "oracion": "San Francisco considera prohibir los robots de entrega en la acera."
    }
  ]
}
```





