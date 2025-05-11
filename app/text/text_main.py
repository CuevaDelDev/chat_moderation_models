from fastapi import APIRouter
from .models import text_moderator_model
from .schemas.message import TextModerationRequest

# Enrutador para la sección de texto
router = APIRouter()

# Definimos la ruta principal
@router.get('/')
async def welcome_text():
    msg = 'Welcome to text moderation'
    return msg 

# Endpoint para la moderación del texto
@router.post('/moderate')
async def moderate(request:TextModerationRequest):
    # EL modelo ya tiene su tokenizador incorporado por lo que solo lo llamamos para predecir
    result = text_moderator_model.model.predict([request.message])
    # Cuerpo de la respuesta
    output = {
        "user": request.user,
        "user_ip": request.ip,
        "message": request.message,
        "result": result # Predicción del modelo 
    }
    return output