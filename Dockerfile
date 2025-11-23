FROM python:3.11-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 10010

ENV FLASK_APP=app.py

CMD ["gunicorn", "--bind", "0.0.0.0:10010", "--workers", "1", "--timeout", "30", "--log-level", "debug", "app:api"]

