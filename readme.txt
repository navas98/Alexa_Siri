Proyecto: Control por Comandos de Voz

Este proyecto permite controlar diversas aplicaciones de tu sistema operativo y gestionar un chatbot interactivo, todo mediante comandos de voz. Utiliza herramientas de reconocimiento y síntesis de voz para escuchar y responder a las órdenes del usuario.

Estructura del Proyecto:

OLLLAMA/
│
├── chat/
│   ├── chat.py          # Lógica principal del chatbot
│   ├── info.py          # Información utilizada por el chatbot
│
├── speak_listen/
│   ├── listen.py        # Captura de audio del usuario
│   ├── speak.py         # Conversión de texto a audio
│
├── main.py              # Archivo principal para gestionar comandos de voz
├── requirements.txt     # Dependencias necesarias para el proyecto

Dependencias:

Instala las dependencias necesarias ejecutando:

pip install -r requirements.txt

Principales librerías utilizadas:
- speech_recognition: Para capturar y procesar audio.
- gtts: Convierte texto en audio para las respuestas.
- pygame: Reproduce el audio generado.

Uso:

Ejecución del Programa Principal
Ejecuta el archivo main.py desde la raíz del proyecto (OLLLAMA/) usando:

python main.py

Funcionalidades:
1. Comandos de voz para abrir aplicaciones comunes:
   - "open word": Abre Microsoft Word.
   - "open excel": Abre Microsoft Excel.
   - "open powerpoint": Abre Microsoft PowerPoint.
   - "open notepad": Abre el Bloc de Notas.
   - "open paint": Abre Microsoft Paint.

2. Gestión del chatbot:
   - "talk": Inicia el chatbot interactivo definido en chat/chat.py.

3. Consulta de la fecha actual:
   - "date": Muestra la fecha actual y la anuncia mediante síntesis de voz.

4. Salir del programa:
   - "goodbye": Termina la ejecución del programa.

Ejemplo de Flujo
1. Inicia el programa con python main.py.
2. Di "open notepad" para abrir el Bloc de Notas.
3. Di "date" para escuchar y ver la fecha actual.
4. Di "talk" para interactuar con el chatbot.
5. Di "goodbye" para salir del programa.

Consideraciones:
- Reconocimiento de voz: Asegúrate de que tu micrófono funcione correctamente.
- Síntesis de voz: Configura altavoces o auriculares para escuchar las respuestas del programa.
- Ejecutar desde la raíz: El programa debe ejecutarse desde la carpeta raíz (OLLLAMA/) para evitar errores de importación.

Contribuciones:

Si deseas contribuir, clona este repositorio, realiza tus cambios y envía un pull request. Todas las contribuciones son bienvenidas.


