import firebase_admin
from firebase_admin import credentials, firestore
import argparse
import json

# Configura las credenciales de Firebase
cred = credentials.Certificate("key/firebase_key.json")
firebase_admin.initialize_app(cred)

# Inicializa la referencia a la base de datos Firestore
db = firestore.client()

def insertar_datos(datos):
    for coleccion, documentos in datos.items():
        # Obtiene una referencia a la colección
        coleccion_ref = db.collection(coleccion)

        for documento in documentos:
            # Añade cada documento como un elemento independiente en la colección
            nuevo_documento_ref = coleccion_ref.add(documento)
            print(f"Documento insertado en la colección '{coleccion}' con ID: {nuevo_documento_ref[1].id}")

def cargar_datos_desde_json(ruta_json):
    with open(ruta_json, 'r') as archivo:
        datos = json.load(archivo)
    return datos

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Insertar datos en Firestore desde un archivo JSON")
    parser.add_argument("--ruta-json", required=True, help="Ruta del archivo JSON con los datos")

    args = parser.parse_args()

    datos_desde_json = cargar_datos_desde_json(args.ruta_json)

    insertar_datos(datos_desde_json)
