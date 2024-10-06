# Use the latest Ubuntu image
FROM ubuntu:latest

# Set environment variables to avoid prompts during installation
ENV DEBIAN_FRONTEND=noninteractive

# Update the package list and install Apache, PHP, and Vim
RUN apt-get update && \
    apt-get install -y apache2 php vim && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copy the web directory content to the Apache web root
COPY ./web /var/www/html

# Expose port 80
EXPOSE 80

# Start the Apache server
CMD ["apache2ctl", "-D", "FOREGROUND"]