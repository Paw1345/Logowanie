# Używamy oficjalnego obrazu Pythona
FROM python:3.9-slim

# Ustawiamy katalog roboczy
WORKDIR /app

# Kopiujemy pliki do kontenera
COPY . .

# Instalujemy zależności
RUN pip install --upgrade pip

RUN pip install -r requirements.txt


# Ustawiamy zmienną środowiskową, aby upewnić się, że Flask działa poprawnie
ENV FLASK_APP=app.py

# Uruchamiamy aplikację
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]

