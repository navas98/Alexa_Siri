import gtts
import pygame
import os
import sys
from io import StringIO

def speak(text):
    try:
        tts = gtts.gTTS(text)
        temp_file = "./temp.mp3"
        tts.save(temp_file)

        # Redirigir salida estándar para eliminar el mensaje de pygame
        original_stdout = sys.stdout
        sys.stdout = StringIO()

        # Usar pygame para reproducir el archivo de audio
        pygame.mixer.init()
        pygame.mixer.music.load(temp_file)
        pygame.mixer.music.play()

        # Restaurar la salida estándar
        sys.stdout = original_stdout

        # Esperar hasta que termine la reproducción
        while pygame.mixer.music.get_busy():
            continue

        # Detener y liberar el archivo
        pygame.mixer.music.stop()
        pygame.mixer.quit()

        # Eliminar el archivo temporal
        os.remove(temp_file)
    except Exception as e:
        print("Error: ", e)
