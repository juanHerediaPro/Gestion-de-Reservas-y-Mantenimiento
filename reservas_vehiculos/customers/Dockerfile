# reservas_vehiculos/customers/Dockerfile

FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PORT 8080 

WORKDIR /usr/src/app

# Copia los requisitos desde su ubicación relativa al contexto ('customers/')
COPY customers/requirements.txt . 
RUN pip install --no-cache-dir -r requirements.txt

# Copia TODO el contenido del contexto (incluye 'customers/' y 'reservas_vehiculos/')
COPY . /usr/src/app/

# CRÍTICO: Configura el PYTHONPATH para que Python encuentre el módulo principal anidado.
# Esto resuelve: ModuleNotFoundError: No module named 'reservas_vehiculos'
ENV PYTHONPATH=/usr/src/app/reservas_vehiculos

# Ejecuta Gunicorn (que ahora puede encontrar el módulo)
CMD exec gunicorn --bind :$PORT --workers 2 --threads 4 reservas_vehiculos.wsgi