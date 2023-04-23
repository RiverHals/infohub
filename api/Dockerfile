FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8
WORKDIR /app
COPY ./api /app/api
COPY ./requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt

COPY . .
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]
docker build -t myapi .
docker run -d --name myapi-container -p 80:80 myapi