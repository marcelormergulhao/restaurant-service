FROM python:3.8-alpine3.15

WORKDIR /app

COPY . /app/
RUN pip install -r requirements.txt

ENTRYPOINT python app.py