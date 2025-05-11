from pydantic import BaseModel

class ImgModerationRequest(BaseModel):
    user: str
    ip: str
    img: str