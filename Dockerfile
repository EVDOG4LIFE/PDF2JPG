FROM python:3.9-alpine

WORKDIR /app

USER root

COPY requirements.txt .

RUN apk add --no-cache zlib-dev jpeg-dev build-base

RUN pip install --no-cache-dir -r requirements.txt

RUN adduser -D appuser
USER appuser

COPY app.py .
COPY templates/ templates/

EXPOSE 5000

ENTRYPOINT ["python", "app.py"]
