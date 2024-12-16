import speech_recognition as sr

r = sr.Recognizer()

def listen(mic_index=None):
    try:
        if mic_index is not None:
            mic = sr.Microphone(device_index=mic_index)
        else:
            mic = sr.Microphone()

        with mic as source:
            print("Escuchando...")
            r.adjust_for_ambient_noise(source, duration=1)
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
    except Exception as e:
        print(f"Error al escuchar: {e}")
        return None
