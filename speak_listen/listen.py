# Archivo: speak_listen/listen.py
import speech_recognition as sr

def listen(mic_index=None):
    r = sr.Recognizer()
    if mic_index is not None:
        mic = sr.Microphone(device_index=mic_index)
    else:
        mic = sr.Microphone()

    with mic as source:
        print("Escuchando...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio, language="en-US")
            print("You said: ", text)
            return text
        except sr.UnknownValueError:
            print("Sorry, I did not get that.")
            return None
        except sr.RequestError as e:
            print("Sorry, I could not request results: ", e)
            return None