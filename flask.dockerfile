FROM python:3.6
RUN mkdir /web_flask
WORKDIR /root
COPY *.py requirements.txt /web_flask/
COPY models /web_flask/models
COPY views /web_flask/views

RUN pip install -r /web_flask/requirements.txt -i http://pypi.douban.com/simple --trusted-host pypi.douban.com
WORKDIR /web_flask
RUN ls
