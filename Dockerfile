# syntax=docker/dockerfile:1

FROM python:3.7
RUN mkdir /docs
ADD . /docs
WORKDIR /docs
RUN apt-get -y update
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install openssl gcc default-libmysqlclient-dev python3-dev build-essential libpcre3 libpcre3-dev  libssl-dev xorg
RUN apt-get install -y netcat
RUN wget https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6-1/wkhtmltox_0.12.6-1.stretch_amd64.deb
RUN dpkg -i wkhtmltox_0.12.6-1.stretch_amd64.deb; exit 0
RUN apt -f install -y
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . . 
CMD python3 main.py