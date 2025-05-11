import torch
from ..models import img_moderator_model


def classify(img_tensors:dict[str, torch.Tensor]) -> tuple[str, list]:
    """
    Función para clasificar imágenes como nsfw o normal

    Args:
        img_tensors (dict[str, torch.Tensor]): Diccionario con tensores de torch

    Returns:
        tuple (str, list): Devuelve una tupla que contiene la probabilidad de cada clase y la activación de las neuronas de la capa final
    """
    # No calculamos los gradientes en inferencia
    with torch.no_grad():
        
        # Le pasamos los tensores al modelo 
        output = img_moderator_model.model(**img_tensors)
        
        # Obtención de los logits
        logits = output.logits
        
        # Tomo el índice del valor máximo
        predicted_label = logits.argmax(-1).item()
        
        # De acuerdo al índice se toma el label
        result = img_moderator_model.model.config.id2label[predicted_label]
        
        return result, logits