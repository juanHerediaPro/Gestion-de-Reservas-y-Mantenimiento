# reservas_vehiculos/customers/Dockerfile

FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PORT 8080 

WORKDIR /usr/src/app

# Copia los requisitos desde su ubicación relativa al contexto (raíz del repo)
# Esto asume que requirements.txt está en reservas_vehiculos/customers/requirements.txt
COPY reservas_vehiculos/customers/requirements.txt . 
RUN pip install --no-cache-dir -r requirements.txt

# Copia la carpeta principal de Django al workdir
# El código estará en /usr/src/app/reservas_vehiculos
COPY reservas_vehiculos /usr/src/app/reservas_vehiculos

# CRÍTICO: Ejecutar un comando shell para cambiar al directorio del proyecto 
# y luego ejecutar gunicorn. Esto resuelve el ModuleNotFoundError.
CMD sh -c "cd /usr/src/app/reservas_vehiculos && exec gunicorn --bind :$PORT --workers 2 --threads 4 reservas_vehiculos.wsgi"