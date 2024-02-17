FROM alpine:latest
LABEL author="Levent Soykan"

RUN apk add --no-cache apache2-ssl
RUN rm -rf /var/www/localhost/cgi-bin/

RUN echo "Listen 8021" >> /etc/apache2/httpd.conf

EXPOSE 8021

CMD ["/bin/sh", "-c", "exec /usr/sbin/httpd -D FOREGROUND -f /etc/apache2/httpd.conf"]