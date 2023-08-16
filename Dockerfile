FROM python:3.9-alpine

WORKDIR /app

RUN adduser -D appuser
USER appuser

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .
COPY templates/ templates/

EXPOSE 5000

ENTRYPOINT ["python", "app.py"]
