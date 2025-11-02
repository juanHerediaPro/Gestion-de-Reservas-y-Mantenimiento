# reservas_vehiculos/customers/Dockerfile

FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PORT 8080 

# El directorio de trabajo base en el contenedor
WORKDIR /usr/src/app

# --- PASO 1: INSTALAR DEPENDENCIAS ---
# Copia requirements.txt desde su ubicación (customers/requirements.txt)
# y lo nombra 'requirements.txt' en el workdir del contenedor.
COPY customers/requirements.txt . 

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# --- PASO 2: COPIAR TODO EL CÓDIGO ---
# Copia TODO el contenido del contexto (la carpeta 'reservas_vehiculos/')
# al directorio /usr/src/app del contenedor.
COPY . /usr/src/app/

# --- PASO 3: INICIO DE GUNICORN ---
# Gunicorn inicia la aplicación, que ahora puede encontrar
# 'reservas_vehiculos.wsgi' dentro de /usr/src/app/reservas_vehiculos
CMD exec gunicorn --bind :$PORT --workers 2 --threads 4 reservas_vehiculos.wsgi:application