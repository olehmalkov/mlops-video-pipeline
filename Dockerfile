FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY main.py .
COPY extractor.py .
COPY detector.py .
COPY reporter.py .
COPY __init__.py .

ENTRYPOINT ["python", "main.py"]
