from transformers import AutoModelForImageClassification

# Modelo pre-entrenado para la clasificación de imágenes nsfw/normal
model = AutoModelForImageClassification.from_pretrained('Falconsai/nsfw_image_detection')
