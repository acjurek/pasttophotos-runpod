FROM python:3.10-slim

# Zainstaluj wymagania
RUN pip install --no-cache-dir runpod

# Skopiuj pliki do obrazu
WORKDIR /app
COPY handler.py /app

# RunPod szuka handler.py automatycznie
CMD ["python", "-u", "-m", "runpod.serverless.worker", "handler"]
