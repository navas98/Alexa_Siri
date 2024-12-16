from listen_speack.listen import listen
from listen_speack.speak import speak
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Comando de activación
command = "HEY BRO"

if __name__ == "__main__":
    while True:
        text = listen()
        if text:  # Verifica si text tiene contenido
            if command.lower() in text.lower():
                print("Comando reconocido")
                speak("How can I help you?")
            else:
                # Procesar directamente otros comandos
                note = text.lower()
                if "open word" in note:
                    os.system("start winword")
                    speak("Opening Word")
                elif "open excel" in note:
                    os.system("start excel")
                    speak("Opening Excel")
                elif "open powerpoint" in note:
                    os.system("start powerpnt")
                    speak("Opening PowerPoint")
                elif "open notepad" in note:
                    os.system("start notepad")
                    speak("Opening Notepad")
                elif "open paint" in note:
                    os.system("start mspaint")
                    speak("Opening Paint")
                elif "talk" in note:
                    print("Abriendo conversación...")
                    speak("Opening conversation.")
                    # Ejecutar conversacion.py
                    os.system("python /alexa/llama/conversacion.py")
                elif "goodbye" in note:
                    speak("Goodbye!")
                    print("Cerrando asistente...")
                    break
                else:
                    print("Comando no reconocido.")
                    speak("Sorry, I didn't understand that.")
        else:
            print("No input detected. Please try again.")
