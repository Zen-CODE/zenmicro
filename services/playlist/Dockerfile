FROM python:3.7-alpine
COPY . /app
WORKDIR /app

COPY core /app
COPY services/playlist /app
COPY services/playlist/service_requirements.txt /app

RUN pip install -r requirements.txt
RUN pip install -r service_requirements.txt
EXPOSE 8001

CMD ["gunicorn", "-w 2", "--bind=0.0.0.0:8001", "main:app"]