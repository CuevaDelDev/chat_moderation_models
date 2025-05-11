# Imagen base
FROM python:3.11

# Definición del directorio de trabajo
WORKDIR /app

# Copia todos los archivos
COPY . .

# Instalación de las dependencias 
RUN pip install --no-cache-dir -r requirements.txt

# Se expone el puerto 8000 de Docker
EXPOSE 8000

# Se ejecuta el siguiente comando para que se inicie el servidor
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
