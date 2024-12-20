import torch
import json
import re
from transformers import LlamaForCausalLM, LlamaTokenizer

# Ruta al modelo
modelo = "./models"

# Detectar dispositivo
dispositivo = "cuda" if torch.cuda.is_available() else "cpu"

print(f"Dispositivo seleccionado: {dispositivo}")

print("Cargando el modelo y el tokenizador...")
try:
    tokenizer = LlamaTokenizer.from_pretrained(modelo, local_files_only=True)
    model = LlamaForCausalLM.from_pretrained(modelo, local_files_only=True).to(dispositivo)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
    print("Modelo cargado con éxito. Puedes empezar a hacer preguntas.")
    # Bucle de conversación
    while True:
        consulta = input("\nTú: ")
        if consulta.lower() in ["salir", "exit", "quit"]:
            print("¡Hasta luego!")
            break
        try:
            # Instrucción mejorada
            prompt = (
                "Analiza la siguiente frase y devuelve solo el nombre del videojuego y la consola en formato JSON. "
                "Ejemplo: {'consola': 'sega', 'videojuego': 'sonic'}\n"
                f"Frase: {consulta}\nRespuesta JSON:"
            )
            # Tokenizar la entrada
            inputs = tokenizer(prompt, return_tensors="pt").to(dispositivo)
            # Generar respuesta
            outputs = model.generate(
                **inputs,
                max_new_tokens=50,
                pad_token_id=tokenizer.eos_token_id,
                do_sample=True,
                temperature=0.1
            )
            # Extraer la respuesta generada
            respuesta = tokenizer.decode(outputs[0], skip_special_tokens=True)
            # Usar expresión regular para extraer consola y videojuego
            match = re.search(r"(\bde\b|\bel\b|al\b) ([\w\s]+) de la ([\w\s]+)", consulta, re.IGNORECASE)
            if match:
                videojuego = match.group(2).strip()
                consola = match.group(3).strip()
                datos = {"consola": consola.lower(), "videojuego": videojuego.lower()}
                print(f"Datos parseados correctamente: {datos}")
            else:
                print("No se pudo extraer el videojuego y la consola de la consulta.")
                print(f"Respuesta generada por el modelo: {respuesta}")

        except Exception as e:
            print(f"Error durante la generación: {e}")
except Exception as e:
    print(f"Error al cargar el modelo o tokenizador: {e}")
