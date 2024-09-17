FROM python:3.9-slim

WORKDIR /my_app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY /app /my_app

CMD ["python", "app.py"]
