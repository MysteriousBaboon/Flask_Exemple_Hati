FROM python:3.8

WORKDIR /app

# Dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

# Expose port
EXPOSE 5000

# Définir la commande pour démarrer l'application
CMD ["python", "app.py"]
