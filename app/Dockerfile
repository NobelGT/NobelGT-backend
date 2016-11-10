FROM python:2.7
MAINTAINER Cem Gokmen <cgokmen@gatech.edu>

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

VOLUME /data
EXPOSE 9000

CMD twistd --nodaemon -l --python=run_server.py