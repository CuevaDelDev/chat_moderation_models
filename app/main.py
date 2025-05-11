from fastapi import FastAPI
from .text import text_main
from .img import img_main
from fastapi.middleware.cors import CORSMiddleware

# Instancia de la api
app = FastAPI()

# Permitimos peticiones de cualquier dominio
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Definimos la ruta principal 
@app.get('/')
async def root():
    return 'Hey'

# Incluimos los routers para las demás rutas
app.include_router(text_main.router, prefix='/text', tags=['Text moderation'])
app.include_router(img_main.router, prefix='/image', tags=['Img moderation'])


