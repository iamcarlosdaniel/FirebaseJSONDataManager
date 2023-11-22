# FirebaseJSONDataManager

Para ejecutar este programa en Python, sigue estos pasos:

1. **Instalar las dependencias:**
   Asegúrate de tener instalada la biblioteca `firebase-admin` en tu entorno. Puedes instalarla ejecutando el siguiente comando en tu terminal:

   ```bash
   pip install firebase-admin
   ```

2. **Crear un archivo JSON con datos:**
   Asegúrate de tener un archivo JSON con los datos que deseas insertar en Firestore. Luego, guarda la ruta del archivo.

3. **Configurar la clave de Firebase:**
   Asegúrate de tener la clave de Firebase (`firebase_key.json`) en la misma carpeta que tu script Python o proporciona la ruta correcta en la línea `cred = credentials.Certificate("key/firebase_key.json")`.

4. **Ejecutar el script:**
   Abre tu terminal, navega a la ubicación del script Python y ejecútalo con el intérprete de Python. Por ejemplo:

   ```bash
   python tu_script.py --ruta-json ruta_de_tu_archivo_json.json
   ```

   Asegúrate de reemplazar `tu_script.py` con el nombre de tu script Python y `ruta_de_tu_archivo_json.json` con la ruta real de tu archivo JSON.

   Este comando utiliza el módulo `argparse` para manejar argumentos de línea de comandos y espera que proporciones la ruta del archivo JSON usando el argumento `--ruta-json`.

Después de ejecutar el script, deberías ver mensajes de salida que indican que los documentos han sido insertados en Firestore.
