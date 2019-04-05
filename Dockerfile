FROM python:3.5.7

WORKDIR /home/demo
COPY . .
EXPOSE 5000

CMD ["bash"]
