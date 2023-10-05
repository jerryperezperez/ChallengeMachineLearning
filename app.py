from collections import OrderedDict

from flask import Flask, request, jsonify

import spacy

# Se inicializa el modelo SpaCy empleando lenguaje en español
modelo = spacy.load("es_core_news_sm")

# Se define la instancia de la aplicacion Flask
app = Flask(__name__)

# Se define la ruta del servicio que procesa las oraciones recibidas de la peticion y retorna las entidades encontradas
@app.route('/procesar', methods=['POST'])
def reconocer_entidades():
    """Servicio que recibe una lista de oraciones y retorna las entidades encontradas por el modelo con su respectiva
    oracion"""
    try:
        # Se extraen los datos de la peticion, debe contener una llave con el nombre de oraciones que incluya las oraciones por procesar
        #
        datos = request.get_json()
        oraciones = datos['oraciones']

        # Se crea la variable lista que almacenará los resultados de cada oracion
        resultados = []

        # Se iteran las oraciones y se extraen las entidades encontradas por el modelo
        for oracion in oraciones:
            doc = modelo(oracion)
            # Se almacenan las entidades nombradas empleando comprehensive dict
            entidades = {ent.text: ent.label_ for ent in doc.ents}
            # Se agrega la oracion y sus respectivas entidades empleando un diccionario
            resultados.append(OrderedDict([
                ("oracion", oracion),
                ("entidades", entidades)
            ]))

        # Se devuelven los resultados almacenados en la lista de resultados en formato JSON
        return jsonify({'resultado': resultados})

    # Se maneja el error generado al intentar reconocer las entidades
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run()
