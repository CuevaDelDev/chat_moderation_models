from fastapi import APIRouter
from .schemas.img import ImgModerationRequest
from .services import moderation_service, process_img

# Enrutador para imagen
router = APIRouter()

# Definición la ruta principal 
@router.get('/')
async def welcome_text():
    msg = 'Welcome to img moderation'
    return msg 

# Endpoint para la moderación de imágenes
@router.post('/moderate')
async def moderate(request: ImgModerationRequest):
    # Procesamiento de la imagen
    img = process_img.process_img(request.img)
    
    # Predicción de la imagen
    result, logits = moderation_service.classify(img)
    
    # Cuerpo del output
    result = {
        "user": request.user,
        "user_ip": request.ip,
        "img_path": request.img,
        "logits": logits.tolist(), 
        "result": result
    }
    
    return result