# reservas_vehiculos/customers/Dockerfile
FROM python:3.11-slim
# ... (variables de entorno)

# 1. El WORKDIR debe apuntar a la raíz donde está la carpeta 'reservas_vehiculos'
# Si el COPY es COPY . /usr/src/app/, entonces el WORKDIR correcto es /usr/src/app/
WORKDIR /usr/src/app 

# Copia de requisitos y instalación (usando el contexto ampliado de Step 2)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia TODO el contenido del contexto (incluyendo ambas carpetas: customers/ y reservas_vehiculos/)
COPY . /usr/src/app/ 

# CRÍTICO: Ajustar el CMD para apuntar al módulo wsgi dentro de la carpeta
# (El nombre del módulo wsgi ahora es 'reservas_vehiculos.wsgi' que está en /usr/src/app/reservas_vehiculos/)
CMD exec gunicorn --bind :$PORT --workers 2 --threads 4 reservas_vehiculos.wsgi