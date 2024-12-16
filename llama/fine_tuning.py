import torch
from transformers import LlamaForCausalLM, LlamaTokenizer, Trainer, TrainingArguments
from datasets import load_dataset
from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training

# Ruta al modelo y archivo de datos
modelo = "./models"
datos_entrenamiento = "./data/datos.json"

print("Cargando el modelo y el tokenizador...")
tokenizer = LlamaTokenizer.from_pretrained(modelo, local_files_only=True)
model = LlamaForCausalLM.from_pretrained(modelo, local_files_only=True)

# Preparar el modelo para entrenamiento con PEFT (k-bit training)
model = prepare_model_for_kbit_training(model)

# Configurar el token de padding
if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token

# Cargar el dataset
dataset = load_dataset("json", data_files=datos_entrenamiento)

# Preprocesar los datos
def preparar_datos(batch):
    texto = f"Pregunta: {batch['input']}\nRespuesta: {batch['output']}"
    tokens = tokenizer(texto, truncation=True, padding="max_length", max_length=512)
    tokens["labels"] = tokens["input_ids"].copy()
    return {
        "input_ids": tokens["input_ids"],
        "attention_mask": tokens["attention_mask"],
        "labels": tokens["labels"]
    }

# Aplicar preprocesamiento al dataset
train_dataset = dataset["train"].map(preparar_datos)

# Configurar PEFT con LoRA
peft_config = LoraConfig(
    r=16,
    lora_alpha=32,
    target_modules=["q_proj", "v_proj"],
    lora_dropout=0.1,
    bias="none",
    task_type="CAUSAL_LM"
)

# Aplicar PEFT al modelo
model = get_peft_model(model, peft_config)

# Configurar los argumentos de entrenamiento
training_args = TrainingArguments(
    output_dir="./resultados",
    per_device_train_batch_size=4,
    num_train_epochs=3,
    learning_rate=2e-5,
    logging_dir="./logs",
    fp16=torch.cuda.is_available(),
    save_steps=500,
    save_total_limit=2
)

# Crear el Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    tokenizer=tokenizer
)

# Iniciar el entrenamiento
print("Iniciando el entrenamiento con PEFT y LoRA...")
trainer.train()

# Guardar el modelo ajustado
model.save_pretrained("./modelo_ajustado")
tokenizer.save_pretrained("./modelo_ajustado")
print("Entrenamiento completado y modelo guardado.")
