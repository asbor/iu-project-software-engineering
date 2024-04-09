# Description: Dockerfile for the FastAPI application
# Author: Asbjorn Bordoy
# Date: 2024-apr-03
# Version: 1.0

# Note: This Dockerfile is used to build a Docker image for the FastAPI application
#       The image is based on the Alpine Linux distribution and uses the uvicorn server
#       The image is built in two stages, the first stage installs the required packages
#       and the second stage runs the uvicorn server

# Usage: docker build -f docker/Dockerfile -t docker-hoppy-brew-app-image .


# Stage 1: Build the image
FROM alpine:3.17 as builder
RUN apk add --no-cache python3 py3-pip libpq postgresql-client curl
RUN adduser -D dbs
USER dbs

# Set the working directory
WORKDIR /home/dbs
COPY . /home/dbs/app

# Install requirements
RUN pip3 install -r requirements.txt --no-cache-dir

# Expose port 8000 for the FastAPI application
EXPOSE 8000

# Run uvicorn server
CMD /home/dbs/.local/bin/uvicorn app/main:app --reload --host 0.0.0.0