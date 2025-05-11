# API de moderación para [chat_global](https://github.com/CuevaDelDev/public_chat)

Para correr la API, se debe ejecutar el siguiente comando 

`docker build -t chat_api .`

Una vez se haya creando la imagen debemos correr un contenedor con la imagen

`docker run -p 8000:8000 chat_api`

Para realizar una inferencia de texto se necesita hacer una petición `POST` a la ruta `/text/moderate` con la siguiente estructura en el body:
    
    {
        user: str, 
        ip: str,    
        message: str
    }

Y para realizar una inferencia con imágenes se debe hacer una petición `POST` a la ruta `/image/moderate` (se necesita que la imagen haya sido codifica a base64)

    {
        user: str, 
        ip: str,    
        img: str
    }
