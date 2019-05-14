#THE ANATOMY OF A DOCKERFILE
# This tells docker from what image is this being built.
# Remember the layered architecture this is the "base layer"
# For this specific image.
# Images can come from registries, or from your own computer.
FROM python:3.6-slim

RUN mkdir /app
WORKDIR /app

# The run commands are those that are executed when the image
# is being built for the first time, but aren't run on boot
RUN echo "hello world!"

# Copies the source folder from the host OS to the destination
# folder of the running docker container.
COPY . .


CMD python app.py


