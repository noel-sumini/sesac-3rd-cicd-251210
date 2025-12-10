FROM python:3.12-slim

WORKDIR /home

COPY ./requirements.txt /home/requirements.txt
COPY ./main.py /home/main.py
COPY ./Dockerfile /home/Dockerfile


RUN pip install -r ./requirements.txt

EXPOSE 8888

CMD [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8888" ]
