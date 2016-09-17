FROM python:3.5.2
MAINTAINER EINDEX snowstarlbk@gmail.com

COPY  . /docker
WORKDIR /docker
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt -i http://pypi.douban.com/simple --trusted-host pypi.douban.com

WORKDIR src

EXPOSE 5000
CMD ls
ENTRYPOINT  gunicorn -c gun.py wsgi:app