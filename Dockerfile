FROM php:7.4-apache

# Install mysqli extension
RUN docker-php-ext-install mysqli

# Copy application files into the container
COPY ./web /var/www/html
