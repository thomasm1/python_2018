# /usr/bin/bash
docker ps | grep -v CONTAINER | awk '{print $1}' | xargs docker stop
docker build ./ -f ./Dockerfile-base -t example-base:latest
docker build ./ -f ./Dockerfile-python -t python-example
docker build ./ -f ./Dockerfile-flask -t flask-example
docker build ./ -f ./Dockerfile-django -t django-example
docker build ./ -f ./Dockerfile-chalice -t chalice-example

