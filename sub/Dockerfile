FROM python:3.8

RUN apt-get update && \
    apt-get install -y cron && \
    apt-get install -y nano

WORKDIR /sub

COPY . .

RUN /usr/local/bin/python -m pip install --upgrade pip

#ADD requirements.txt /app

RUN pip --no-cache-dir install -r requirements.txt

ENV TZ=Asia/Taipei

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

#COPY ./app /app

#COPY crontab /etc/cron.d/script-cron
RUN chmod -R 777 /sub/app
#ADD gunicorn_config.py /app
RUN chmod +x /sub/exec.sh

ADD crontabfile /etc/cron.d/my-cron

RUN chmod 0644 /etc/cron.d/my-cron

RUN touch /var/log/cron.log

CMD cron && tail -f /var/log/cron.log

#RUN crontab -l | { cat; echo "*/1 * * * * /bin/sh /app/entrypoint.sh"; } | crontab -

#CMD cron
#EXPOSE 6000

#ADD entrypoint.sh /app

#RUN chmod +x /etc/cron.d/script-cron

#CMD ["cron", "-f"]
#ENTRYPOINT ["sh", "entrypoint.sh"]
#ENTRYPOINT ["python", "server.py"]
#CMD python ./server.py
