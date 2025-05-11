from pydantic import BaseModel

# Esquema para la moderación de texto
class TextModerationRequest(BaseModel):
    user: str
    ip: str
    message: str