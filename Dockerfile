FROM ubuntu:16.04
EXPOSE 8080
RUN apt-get update
RUN apt-get install -y python-pip
RUN mkdir -p /srv/helloworld/code
WORKDIR /srv/helloworld/code
COPY . /srv/helloworld/code
RUN pip install -U .
CMD helloworld
