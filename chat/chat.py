import sys
import os

# Agregar la carpeta raíz al sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from chat.info import info  # Importar info desde la carpeta chat
from speak_listen.listen import listen  # Importar listen desde la carpeta speak_listen
from speak_listen.speak import speak  # Importar speak desde la carpeta speak_listen
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = """
Answer the question below in english.

Here is the family information:
{info}

{context}

Question: {question}

Answer:
"""

# Define el modelo y la plantilla del prompt
model = OllamaLLM(model="phi3")
prompt = ChatPromptTemplate.from_template(template)

# Crear una cadena (chain) que conecte el prompt con el modelo
chain = prompt | model

def chat():
    print("Welcome to the chatbot")
    speak("Welcome to the chatbot")
    context = ""  # Contexto de la conversación

    while True:
        print("Listening for your question...")
        question = listen()  # Escucha la pregunta del usuario
        if question is None:
            speak("I didn't catch that. Could you repeat?")
            continue

        if "stop" in question.lower():  # Comando para detener el chat
            speak("Goodbye! Have a great day!")
            break

        # Invocar la cadena con los datos proporcionados
        try:
            result = chain.invoke({"info": info, "context": context, "question": question})
            print("Bot:", result)
            speak(result)  # Respuesta del bot por voz

            # Actualizar el contexto con la nueva interacción
            context += f"You: {question}\nBot: {result}\n"
        except Exception as e:
            print("Error while processing your request:", e)
            speak("Sorry, I encountered an error while processing your request.")

