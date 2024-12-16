# speak.py
import gtts
from playsound import playsound
import os

def speak(text):
    try:
        tts = gtts.gTTS(text)
        temp_file = "./temp.mp3"
        tts.save(temp_file)
        playsound(temp_file)
        os.remove(temp_file)
    except Exception as e:
        print("Error: ", e)
