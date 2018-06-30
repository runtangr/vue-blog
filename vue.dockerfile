FROM node:8.9.2
RUN mkdir /web-blog
COPY package.json package-lock.json /web-blog/
WORKDIR /web-blog
RUN npm install
COPY . /web-blog
RUN ls 
