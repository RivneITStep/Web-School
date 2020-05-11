FROM node:latest

MAINTAINER vasiazozulia

COPY  . /var/www
WORKDIR /var/www

RUN npm install
RUN npm install -g gulp

ENTRYPOINT [ "gulp" ]