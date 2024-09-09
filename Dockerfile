# Wybierz obraz bazowy
FROM python:3.9-slim

# Ustaw katalog roboczy
WORKDIR /app

# Skopiuj pliki do kontenera
COPY requirements.txt ./
RUN pip install -r requirements.txt

# Skopiuj resztę plików do kontenera
COPY . .

# Uruchom aplikację
CMD ["python", "app.py"]
