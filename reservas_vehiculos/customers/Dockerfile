# reservas_vehiculos/customers/Dockerfile

FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PORT 8080 

# El directorio de trabajo base en el contenedor
WORKDIR /usr/src/app

# Copia los requisitos desde la raíz del repo
COPY reservas_vehiculos/customers/requirements.txt . 
RUN pip install --no-cache-dir -r requirements.txt

# Copia toda la carpeta 'reservas_vehiculos' al workdir
COPY reservas_vehiculos /usr/src/app/
# ...
CMD exec gunicorn --bind :$PORT --workers 2 --threads 4 reservas_vehiculos.wsgi