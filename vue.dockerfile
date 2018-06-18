FROM node:8.9.2
RUN mkdir /vue-blog
COPY package.json package-lock.json /vue-blog/
WORKDIR /vue-blog
RUN npm install
COPY . /vue-blog
RUN ls 
