# Archivo: main.py
import os
from datetime import datetime
from speak_listen.listen import listen
from speak_listen.speak import speak
from chat.chat import chat
if __name__ == "__main__":
    last_command = None  # Para detectar comandos repetidos

    while True:
        text = listen()  # Escuchar comandos
        if text:
            if last_command == text.lower():  # Comprobar si el comando es repetido
                print("Comando repetido, ignorado.")
                continue

            last_command = text.lower()  # Actualizar el último comando

            if "goodbye" in text.lower():  # Comando para salir
                print("Goodbye!")
                speak("Goodbye! Have a great day!")
                break

            # Comandos para abrir aplicaciones
            elif "open word" in text.lower():
                os.system("start winword")
            elif "open excel" in text.lower():
                os.system("start excel")
            elif "open powerpoint" in text.lower():
                os.system("start powerpnt")
            elif "open notepad" in text.lower():
                os.system("start notepad")
            elif "open paint" in text.lower():
                os.system("start mspaint")
            elif "talk" in text.lower():
                chat()
            # Consulta de fecha actual
            elif "date" in text.lower():
                now = datetime.now()
                current_date = now.strftime("%d/%m/%Y")
                print(f"Today's date is: {current_date}")
                speak(f"Today's date is {current_date}")
            else:
                print("Comando no reconocido.")
                speak("Sorry, I did not understand that command.")
