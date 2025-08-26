FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8002

WORKDIR /app
CMD ["uvicorn", "not_interesting_subscriber.app.main:app", "--host", "0.0.0.0", "--port", "8002"]