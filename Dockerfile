FROM python:3.9-slim

WORKDIR /app

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y \
    gcc \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Copiar requirements
COPY backend/requirements.txt .

# Instalar dependencias Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar aplicación
COPY backend/ ./backend/
COPY frontend/ ./frontend/

# Exponer puerto
EXPOSE 5000

# Comando por defecto
CMD ["python", "backend/app.py"]
