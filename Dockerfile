FROM python:3.9-slim

WORKDIR /app

COPY app.py .
COPY templates/ templates/
COPY requirements.txt .

RUN pip install -r requirements.txt

CMD ["python", "app.py"]