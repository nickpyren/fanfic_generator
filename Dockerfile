# syntax=docker/dockerfile:1
from python:3.8-slim-buster
WORKDIR /fanfic_generator
COPY . .
RUN pip install -r requirements.txt
EXPOSE 8000
CMD [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]