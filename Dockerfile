FROM python:3.9-alpine

WORKDIR /app

USER root

COPY requirements.txt .

# Installing system dependencies
RUN apk add --no-cache \
    zlib-dev \
    jpeg-dev \
    libjpeg-turbo-dev \
    build-base \
    poppler-utils

# Installing Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Creating a non-root user and switching to it
RUN adduser -D appuser
USER appuser

# Copying the application files to the container
COPY app.py .
COPY templates/ templates/

# Exposing the application port
EXPOSE 5000

ENTRYPOINT ["python", "app.py"]
