# Wybierz obraz bazowy
FROM python:3.9-slim

# Ustaw katalog roboczy
WORKDIR /app

# Skopiuj pliki do kontenera
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .

# Uruchom aplikację
CMD ["python", "app.py"]
