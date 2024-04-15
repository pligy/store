FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install --progress-bar off -r requirements.txt
#COPY . .
COPY ./app /app

EXPOSE 8000