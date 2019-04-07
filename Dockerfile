FROM python:3.5.7

WORKDIR /home/demo
COPY . .
EXPOSE 5000
RUN pip install -r requirements.txt

CMD ["python", "flask_app.py"]
