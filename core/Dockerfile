FROM python:3.7-alpine
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 8001

CMD ["gunicorn", "-w 4", "--bind=0.0.0.0:8001", "main:app"]