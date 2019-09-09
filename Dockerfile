FROM python:3.7-alpine

# dont create bytecode files
ENV PYTHONDONTWRITEBYTECODE 1
# don't buffer, get log messages immediately
ENV PYTHONUNBUFFERED 1

# add bash for running commands via docker
RUN apk add --no-cache bash

# upgrade pip and setuptools
RUN pip install --upgrade pip setuptools twine

# set the working directory to /app
WORKDIR /app

# copy the current directory contents into the container at /app
COPY . /app

# install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt
