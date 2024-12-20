import torch
import json
import re
from transformers import LlamaForCausalLM, LlamaTokenizer

# Ruta al modelo
modelo = "./modelo_ajustado"

# Detectar dispositivo
dispositivo = "cuda" if torch.cuda.is_available() else "cpu"

print(f"Dispositivo seleccionado: {dispositivo}")

print("Cargando el modelo y el tokenizador...")
try:
    tokenizer = LlamaTokenizer.from_pretrained(modelo, local_files_only=True)
    model = LlamaForCausalLM.from_pretrained(modelo, local_files_only=True).to(dispositivo)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
    print("Modelo cargado con éxito. Puedes empezar a conversar.")

    # Bucle de conversación
    while True:
        consulta = input("\nTú: ")
        if consulta.lower() in ["salir", "exit", "quit"]:
            print("¡Hasta luego!")
            break
        try:
            # Instrucción específica para el modelo
            prompt = (
                f"Obten la cancion"
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

            # Obtener solo la nueva parte generada por el modelo
            nueva_respuesta = respuesta[len(prompt):].strip()

            # Imprimir la respuesta
            print(f"Asistente: {nueva_respuesta}")

        except Exception as e:
            print(f"Error durante la generación: {e}")

except Exception as e:
    print(f"Error al cargar el modelo o tokenizador: {e}")
