FROM nginx

RUN mkdir -p /var/www/html/
COPY static/ /var/www/html/static/
RUN rm /etc/nginx/conf.d/default.conf
COPY local.conf /etc/nginx/conf.d/.

EXPOSE 80

#CMD ["service nginx restart"]
