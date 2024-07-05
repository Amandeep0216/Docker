From python:3.9-slim
WORKDIR /app/usr/src
COPY . .
CMD ["python", "./app.py"]