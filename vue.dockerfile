FROM node:9.11.1

RUN mkdir /vue-blog
COPY . /vue-blog
WORKDIR /vue-blog
RUN ls