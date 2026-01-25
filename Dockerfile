FROM python:3.11

WORKDIR /app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV FLASK_APP=app.py

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . .

EXPOSE 10010

CMD ["gunicorn", "--bind", "0.0.0.0:10010", "--workers", "1", "--timeout", "30", "--log-level", "debug", "app:api"]

