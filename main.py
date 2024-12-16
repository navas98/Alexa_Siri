from listen_speack.listen import listen
from listen_speack.speak import speak
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Activation command
command = "hello"

if __name__ == "__main__":
    while True:
        text = listen()
        if text:  # Check if text contains content
            if command.lower() in text.lower():
                print("Command recognized")
                speak("How can I help you?")
            else:
                # Directly process other commands
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
                elif "open paint" in note:
                    os.system("start mspaint")
                    speak("Opening Paint")
                elif "talk" in note:
                    print("Opening conversation...")
                    speak("Opening conversation.")
                    # Execute conversacion.py
                    os.system("python /alexa/llama/conversacion.py")
                elif "goodbye" in note:
                    speak("Goodbye!")
                    print("Closing assistant...")
                    break
                else:
                    print("Command not recognized.")
                    speak("Sorry, I didn't understand that.")
        else:
            print("No input detected. Please try again.")
