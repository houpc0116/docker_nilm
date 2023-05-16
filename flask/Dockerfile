FROM python:3.8.16-alpine3.17

WORKDIR /app

RUN /usr/local/bin/python -m pip install --upgrade pip

ADD requirements.txt /app

RUN pip --no-cache-dir install -r requirements.txt

COPY ./app /app

ADD gunicorn_config.py /app

#EXPOSE 5000

ADD entrypoint.sh /app

RUN chmod +x entrypoint.sh

ENTRYPOINT ["sh", "entrypoint.sh"]
#ENTRYPOINT ["python", "server.py"]
#CMD python ./server.py
