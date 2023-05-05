FROM python:3.8
# 设置 python 环境变量
ENV PYTHONUNBUFFERED 1

RUN apt-get update && \
    apt-get install -y cron && \
    apt-get install -y nano

# 安裝所需的系統庫
RUN apt-get update && apt-get install -y build-essential

RUN /usr/local/bin/python -m pip install --upgrade pip

RUN mkdir /api

WORKDIR /api

ADD requirements.txt /api
#COPY . /api

RUN pip --no-cache-dir install -r requirements.txt

ADD . /api

ENV TZ=Asia/Taipei

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

ADD entrypoint.sh /api

RUN chmod +x entrypoint.sh

ENTRYPOINT ["sh", "entrypoint.sh"]

# 指定uwsgi配置文件位置
#ENV UWSGI_INI /api/web_api_2/uwsgi.ini

#EXPOSE 8000

# 執行 makemigrations
#RUN python manage.py makemigrations

#RUN python manage.py migrate

# 啟動uwsgi
#CMD ["uwsgi", "--ini", "/api/web_api_2/uwsgi.ini"]
