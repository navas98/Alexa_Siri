import sys
import os

# Obtener la ruta raíz del proyecto ALEXA
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(BASE_DIR)

from listen_speack.listen import listen
from listen_speack.speak import speak

import torch
from transformers import LlamaForCausalLM, LlamaTokenizer
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Ruta corregida al modelo ajustado
fine_tuned_model = os.path.join(BASE_DIR, "llama", "models")

# Cargar modelo y tokenizer
print("Loading the fine-tuned model...")
tokenizer = LlamaTokenizer.from_pretrained(fine_tuned_model)
model = LlamaForCausalLM.from_pretrained(fine_tuned_model).to("cuda" if torch.cuda.is_available() else "cpu")

print("Model loaded. You can start asking questions.")

# Historial de conversación
history = "You are a helpful assistant. Respond clearly and precisely to the user's questions.\n"

# Bucle principal
while True:
    try:
        print("\nListening for your question...")
        user_input = listen()  # Capturar audio desde el micrófono

        if not user_input:
            print("No input detected. Try again.")
            continue
        
        # Comprobar si el usuario quiere salir
        if "goodbye" in user_input.lower() or "quit" in user_input.lower() or "exit" in user_input.lower():
            print("Goodbye!")
            speak("Goodbye!")
            break  # Terminar el programa
        print(f"You: {user_input}")
        history += f"User: {user_input}\nAssistant:"

        # Tokenizar y generar respuesta
        inputs = tokenizer(history, return_tensors="pt").to("cuda" if torch.cuda.is_available() else "cpu")
        outputs = model.generate(
            **inputs,
            max_new_tokens=60,
            pad_token_id=tokenizer.eos_token_id,
            do_sample=True,
            temperature=0.4,
            top_p=0.85,
            repetition_penalty=1.5
        )

        # Decodificar respuesta
        response = tokenizer.decode(outputs[0], skip_special_tokens=True).strip()
        response = response.split(user_input, 1)[-1].strip() if user_input in response else response

        # Validar respuesta
        if len(response.split()) < 3:
            response = "I'm sorry, I don't understand your question. Could you please rephrase it?"

        print(f"Assistant: {response}")
        speak(response)  # Responder con audio
        history += f" {response}\n"

    except KeyboardInterrupt:
        print("\nInterrupted by user. Goodbye!")
        speak("Goodbye!")
        break
    except Exception as e:
        print(f"Error: {e}")
        speak("An error occurred. Please try again.")
