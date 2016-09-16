FROM python:3.5.2
MAINTAINER EINDEX snowstarlbk@gmail.com

COPY  . /src
WORKDIR /src

ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt -i http://pypi.douban.com/simple --trusted-host pypi.douban.com

EXPOSE 5000
ENTRYPOINT  gunicorn -w 4 -b 0.0.0.0:5000 --worker-class=gevent wsgi:app