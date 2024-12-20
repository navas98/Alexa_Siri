import torch
from transformers import LlamaForCausalLM, LlamaTokenizer

# Ruta al modelo ajustado para música
modelo_musica = "./modelo_musica"

print("Cargando el modelo ajustado y el tokenizador...")
try:
    tokenizer = LlamaTokenizer.from_pretrained(modelo_musica, local_files_only=True)
    model = LlamaForCausalLM.from_pretrained(modelo_musica, local_files_only=True).to("cuda" if torch.cuda.is_available() else "cpu")
    print("Modelo y tokenizador cargados correctamente.")
except Exception as e:
    print(f"Error al cargar el modelo o tokenizador: {e}")
    exit(1)

# Bucle para interactuar con el modelo
print("Puedes empezar a hacer preguntas sobre canciones. Escribe 'salir' para terminar.")
while True:
    consulta = input("\nTú: ")
    if consulta.lower() in ["salir", "exit", "quit"]:
        print("¡Hasta luego!")
        break

    try:
        # Crear el prompt
        prompt = f"Analiza la siguiente frase y devuelve sola el nombre de la cancion en formato json Ejemplo: cancion:polePregunta: {consulta}\nRespuesta:"

        # Tokenizar la consulta
        inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

        # Generar respuesta
        outputs = model.generate(
            **inputs,
            max_new_tokens=50,
            pad_token_id=tokenizer.eos_token_id,
            do_sample=True,
            temperature=0.7
        )

        # Decodificar la respuesta
        respuesta = tokenizer.decode(outputs[0], skip_special_tokens=True)

        # Imprimir la respuesta generada
        print(f"Modelo: {respuesta.split('Respuesta:')[-1].strip()}")
    except Exception as e:
        print(f"Error al generar la respuesta: {e}")
