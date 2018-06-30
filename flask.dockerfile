FROM python:3.6
RUN mkdir /web-blog
WORKDIR /root

COPY *.py requirements.txt local_set.tmp /web-blog/
RUN pip install -r /web-blog/requirements.txt -i http://pypi.douban.com/simple --trusted-host pypi.douban.com

COPY . /web-blog


WORKDIR /web-blog
RUN ls
