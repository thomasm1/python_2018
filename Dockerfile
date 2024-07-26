FROM python:3.9-slim

WORKDIR /app

COPY simple_server.py .

CMD ["python", "simple_server.py"]

