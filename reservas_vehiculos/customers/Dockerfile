# Dockerfile
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Puerto estándar de Cloud Run
ENV PORT 8080 

WORKDIR /usr/src/app

# Copia los archivos de requerimientos e instala
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia el código fuente completo del microservicio
COPY . /usr/src/app/

# CRÍTICO: Comando de ejecución con Gunicorn
# Asegúrate de que esta ruta (reservas_vehiculos.wsgi) sea correcta.
# Si el archivo settings.py está en la carpeta 'reservas_vehiculos', esto es correcto.
CMD exec gunicorn --bind :$PORT --workers 2 --threads 4 reservas_vehiculos.wsgi