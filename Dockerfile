FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

COPY ./app /app
COPY ./data /data

RUN pip install -r /app/requirements.txt