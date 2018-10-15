FROM nginx

RUN apt-get update && apt-get upgrade -y && apt-get autoremove && apt-get autoclean
RUN apt-get install -y \
        nano

RUN rm -f /etc/nginx/conf.d/*
RUN rm -f /etc/nginx/nginx.conf
ADD nginx.conf /etc/nginx/nginx.conf
ADD conf.d/default.conf /etc/nginx/conf.d/default.conf
