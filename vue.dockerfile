FROM node:10.4.1

RUN mkdir /vue-blog
COPY . /vue-blog
WORKDIR /vue-blog
RUN npm install