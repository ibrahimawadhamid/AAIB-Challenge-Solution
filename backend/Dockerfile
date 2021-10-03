FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

COPY . /app

# install additional dependencies
COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt