from io import BytesIO
from base64 import b64decode
from transformers import ViTImageProcessor
from PIL import Image
import torch

# Instancia del pre-procesador de imágenes
img_processor = ViTImageProcessor.from_pretrained('Falconsai/nsfw_image_detection')

def process_img(encoded_img:str) -> dict[str, torch.Tensor]:
    """
    Codifica las imágenes antes de que pasen al modelo 

    Args:
        encoded_img (str): Imagen codificada en base64

    Returns:
        dict[str, torch.Tensor]: Devuelve un diccionario con los tensores de la imagen
    """
    # Se decodifica la imagen de base64
    decode_img = b64decode(encoded_img)
    
    # Se carga en memora
    read_img = BytesIO(decode_img)
    
    # Se abre
    opened_img = Image.open(read_img).convert('RGB')
    
    # Se para al procesador
    input = img_processor(images=opened_img, return_tensors='pt')
    
    return input